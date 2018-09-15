
import logging

from steam import SteamClient
from steam.base.msg.emsg import EMsg


logging.basicConfig(format="[%(levelname)s] %(asctime)s: %(name)s: %(message)s",
                    level=logging.DEBUG)

client = SteamClient()


@client.on(EMsg.ClientAccountInfo)
async def account_info(msg):
    print(msg.body)


if __name__ == '__main__':
    try:
        client.login()
        client.run_forever()
    except KeyboardInterrupt:
        logging.info('Waiting client to close')
        client.close()
        logging.info('Client closed')


