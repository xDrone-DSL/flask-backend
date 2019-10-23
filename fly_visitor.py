from logging import info
from lark import Visitor
from pyparrot.Minidrone import Mambo

class Fly(Visitor):
    def __init__(self):
        mamboAddr = "d0:3a:86:9d:e6:5a"
        self.mambo = Mambo(mamboAddr, use_wifi=False)

        info("Trying to connect")
        success = self.mambo.connect(num_retries=3)
        info("Connected: %s" % success)

    def __del(self):
        info("Disconnecting")
        self.mambo.disconnect()

    def takeoff(self, tree):
        info('Taking off')
        self.mambo.safe_takeoff(5)

    def land(self, tree):
        info('Landing')
        self.mambo.safe_land(5)

    def wait(self, tree):
        seconds, = tree.children
        seconds = int(seconds)

        info('Waiting {} seconds'.format(seconds))
        self.mambo.smart_sleep(seconds)
        info('Waited')
