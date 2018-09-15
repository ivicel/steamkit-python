import asyncio
import inspect
import itertools
import logging
from functools import partial
from collections import defaultdict, OrderedDict


class EventEmitter(object):
    EVENT_EMITTER_ERROR = 'event_emitter_error'
    _events = None
    _loop = None

    def __init__(self, loop=None):
        self._events = defaultdict(OrderedDict)
        self._events_once = defaultdict(OrderedDict)
        self._wait_queue = defaultdict(list)
        self._loop = loop or asyncio.get_event_loop()
        self._LOG = logging.getLogger(self.__class__.__name__)

    def on(self, event, f=None):
        def _on(func):
            self.add_event_listener(event, func, func)
            return func

        if f is not None:
            return _on(f)
        else:
            return _on

    def add_event_listener(self, event, k, v):
        self._events[event][k] = v

    def emit(self, event, *args, **kwargs):
        self._LOG.debug("Emit event %s", event)
        result = True if not args else args[0]
        for f in self._wait_queue[event]:
            f.set_result(result)
        self._wait_queue[event].clear()

        callbacks = itertools.chain(self._events[event].values(), self._events_once[event].values())
        del self._events_once[event]
        for f in callbacks:
            if inspect.iscoroutine(f):
                asyncio.ensure_future(f, loop=self._loop)
            elif isinstance(f, partial) and inspect.iscoroutinefunction(f.func):
                asyncio.ensure_future(f(*args, **kwargs), loop=self._loop)
            elif isinstance(f, partial):
                self._loop.call_soon(partial(f, *args, **kwargs))

    async def _coro_func(self, coro):
        try:
            await coro
        except Exception as exc:
            self.emit(self.EVENT_EMITTER_ERROR, exc)

    async def wait(self, event):
        future = self._loop.create_future()
        self._wait_queue[event].append(future)
        try:
            await future
        except:
            return False
        return future.result()

    def once(self, event, f=None):
        def _on(func):
            self._events_once[event][func] = func
            return func

        if f is not None:
            return _on(f)
        else:
            return _on
