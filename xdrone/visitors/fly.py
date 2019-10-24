from logging import info
from lark import Visitor
from pyparrot.Minidrone import Mambo

class Fly(Visitor):
    def __init__(self, mac_addr):
        self.mambo = Mambo(mac_addr, use_wifi=False)

        info("Trying to connect")
        success = self.mambo.connect(num_retries=3)
        info("Connected: %s" % success)

    def __del(self):
        info("Disconnecting")
        self.mambo.disconnect()

    def takeoff(self, tree):
        info('Taking off')
        self.mambo.safe_takeoff(5)
        self.mambo.smart_sleep(1)

    def land(self, tree):
        info('Landing')
        self.mambo.safe_land(5)

    def up(self, tree):
        self.mambo.smart_sleep(1)
        pass

    def down(self, tree):
        self.mambo.smart_sleep(1)
        pass

    def left(self, tree):
        duration, = tree.children
        duration = float(duration)

        self.mambo.fly_direct(roll=-10,
                         pitch=0,
                         yaw=0,
                         vertical_movement=0,
                         duration=duration)
        self.mambo.smart_sleep(1)

    def right(self, tree):
        duration, = tree.children
        duration = float(duration)

        self.mambo.fly_direct(roll=10,
                         pitch=0,
                         yaw=0,
                         vertical_movement=0,
                         duration=duration)
        self.mambo.smart_sleep(1)

    def forward(self, tree):
        duration, = tree.children
        duration = float(duration)

        self.mambo.fly_direct(roll=0,
                         pitch=10,
                         yaw=0,
                         vertical_movement=0,
                         duration=duration)
        self.mambo.smart_sleep(1)

    def backward(self, tree):
        duration, = tree.children
        duration = float(duration)

        self.mambo.fly_direct(roll=0,
                         pitch=-10,
                         yaw=0,
                         vertical_movement=0,
                         duration=duration)
        self.mambo.smart_sleep(1)

    def rotatel(self, tree):
        degrees, = tree.children
        degrees = float(degrees)

        self.mambo.turn_degrees(-degrees)
        self.mambo.smart_sleep(1)

    def rotater(self, tree):
        degrees, = tree.children
        degrees = float(degrees)

        self.mambo.turn_degrees(degrees)
        self.mambo.smart_sleep(1)

    def wait(self, tree):
        seconds, = tree.children
        seconds = float(seconds)

        info('Waiting {} seconds'.format(seconds))
        self.mambo.smart_sleep(seconds)
        info('Waited')
