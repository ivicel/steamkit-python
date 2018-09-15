import logging
import asyncio
import contextlib
from getpass import getpass
from random import choice

from steam.base.msg import ProtoMsg, EMsg
from steam.base.msg.types import EResult
from steam.client.cm import CMClient
from steam.protobufs.steammessages_clientserver_login_pb2 import CMsgClientLogon
from steam.utils.util import ip_to_int


class SteamClient(CMClient):
    """"""
    server_addrs = [
        ("203.80.149.104", 27018),
        ("203.80.149.104", 27017),
        ("180.101.192.249", 27017),
        ("180.101.192.249", 27019),
        ("180.101.192.199", 27019),
        ("203.80.149.68", 27019),
        ("203.80.149.68", 27017),
        ("180.101.192.249", 27018),
        ("203.80.149.104", 27019),
        ("180.101.192.200", 27019),
        ("180.101.192.199", 27017),
        ("203.80.149.68", 27018),
        ("203.80.149.67", 27019),
        ("180.101.192.199", 27018),
        ("203.80.149.67", 27018),
        ("180.101.192.200", 27017),
        ("203.80.149.67", 27017),
        ("180.101.192.200", 27018),
        ("153.254.86.142", 27019),
        ("153.254.86.142", 27018),
        ("153.254.86.143", 27017),
        ("153.254.86.143", 27018),
        ("153.254.86.143", 27019),
        ("153.254.86.142", 27017),
        ("103.28.54.10", 27018),
        ("103.28.54.12", 27019),
        ("103.28.54.12", 27017),
        ("103.28.54.10", 27017),
        ("45.121.186.10", 27018),
        ("103.28.54.12", 27018),
        ("103.28.54.11", 27018),
        ("103.28.54.11", 27017),
        ("45.121.186.11", 27018),
        ("45.121.186.10", 27017),
        ("103.28.54.10", 27019),
        ("45.121.186.10", 27019),
        ("45.121.186.11", 27019),
        ("45.121.186.11", 27017),
        ("103.28.54.11", 27019),
        ("162.254.195.44", 27017),
        ("162.254.195.47", 27018),
        ("162.254.195.44", 27019),
        ("162.254.195.45", 27017),
        ("162.254.195.47", 27017),
        ("162.254.195.46", 27017),
        ("162.254.195.44", 27018),
        ("162.254.195.47", 27019),
        ("162.254.195.46", 27018),
        ("162.254.195.45", 27019),
        ("162.254.195.46", 27019),
        ("162.254.195.45", 27018),
        ("162.254.193.7", 27017),
        ("162.254.193.46", 27018),
        ("162.254.193.6", 27018),
        ("162.254.193.47", 27019),
        ("162.254.193.7", 27018),
        ("162.254.193.47", 27017),
        ("162.254.193.6", 27019),
        ("162.254.193.6", 27017),
        ("162.254.193.47", 27018),
        ("162.254.193.46", 27017),
        ("162.254.193.7", 27019),
        ("162.254.193.46", 27019),
        ("155.133.254.132", 27017),
        ("155.133.254.133", 27018),
        ("155.133.254.132", 27018),
        ("155.133.254.133", 27019),
        ("155.133.254.133", 27017),
        ("205.196.6.67", 27018),
        ("205.196.6.67", 27017),
        ("205.196.6.75", 27019),
        ("155.133.254.132", 27019),
        ("205.196.6.67", 27019),
        ("205.196.6.75", 27018),
        ("205.196.6.75", 27017),
        ("155.133.227.12", 27017),
        ("155.133.227.11", 27019),
        ("155.133.227.11", 27017),
        ("155.133.227.12", 27018),
        ("155.133.227.12", 27019)
    ]

    def __init__(self, loop=None):
        if loop is None:
            loop = asyncio.get_event_loop()
        self._loop = loop
        CMClient.__init__(self, loop)
        self._LOG = logging.getLogger(self.__class__.__name__)

    def login(self, username='', password=''):
        self.username = username
        result = self._loop.run_until_complete(self.connect(self.server))
        print('result =', result)
        if result:
            asyncio.ensure_future(self._async_logon(username, password), loop=self._loop)

    async def _async_logon(self, username, password, login_key=None,
                           two_factor_code=None, auth_code=None,
                           should_remember_password=False):
        while self.connected:
            await self.wait(self.EVENT_CHANNEL_CONNECTED)

            if not username:
                username = input('Please enter your steam account:')

            if not password:
                password = getpass("Please enter your password:")

            self._make_logon_info(username, password, login_key=login_key, two_factor_code=two_factor_code,
                                  auth_code=auth_code, should_remember_password=should_remember_password)

            msg = await self.wait(EMsg.ClientLogOnResponse)
            print('Got EMsg.ClientLogOnResponse: ', msg.body.eresult)
            if msg.body.eresult == EResult.OK:
                self._LOG.debug('Successful logged in with %s' % self.username)
                break

            self.disconnect()
            if msg.body.eresult == EResult.InvalidPassword:
                while True:
                    password = getpass("Invalid password, please enter password again:")
                    if password:
                        break

            elif msg.body.eresult in (EResult.AccountLoginDeniedNeedTwoFactor,
                                      EResult.AccountLogonDenied,
                                      EResult.TwoFactorCodeMismatch):
                while True:
                    code = input("Please input your two-factor code:")
                    if code:
                        break
                if msg.body.eresult == EResult.AccountLogonDenied:
                    auth_code = code
                else:
                    two_factor_code = code

            await self.connect(self.server)

    @property
    def server(self):
        """:return cm server"""
        return choice(self.server_addrs)

    def _make_logon_info(self, username, password, login_key=None,
                         two_factor_code=None,
                         auth_code=None,
                         should_remember_password=False):
        print('\033[30mlogin with (%s, %s, %s, %s)\033[0m' % (username, password, two_factor_code, auth_code))
        clogin = ProtoMsg(EMsg.ClientLogon)
        clogin.header.steamid = 76561197960265728

        clogin.body = CMsgClientLogon()
        clogin.body.obfustucated_private_ip = ip_to_int(self.connection.local_address) ^ 0xBAADF00D
        clogin.body.account_name = username
        clogin.body.password = password
        if login_key:
            clogin.login_key = login_key

        clogin.body.protocol_version = 65579
        clogin.body.client_os_type = 16
        clogin.body.client_package_version = 1771
        clogin.body.should_remember_password = should_remember_password
        clogin.body.supports_rate_limit_response = True
        clogin.body.steam2_ticket_request = False
        clogin.body.machine_name = "pysteam"
        clogin.body.client_language = 'english'
        clogin.body.eresult_sentryfile = 9

        if two_factor_code:
            clogin.body.two_factor_code = two_factor_code

        if auth_code:
            clogin.body.auth_code = auth_code

        self.send(clogin)

    def close(self):
        self.disconnect()
        for t in asyncio.Task.all_tasks(loop=self._loop):
            if t.cancel():
                with contextlib.suppress(asyncio.CancelledError):
                    self._loop.run_until_complete(t)

        if self._loop.is_running():
            self._loop.close()

    def run_forever(self):
        self._loop.run_forever()
