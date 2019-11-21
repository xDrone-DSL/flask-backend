from logging import info
from lark import Visitor
from pyparrot.Minidrone import Mambo
from math import floor

class Fly(Visitor):
    def __init__(self, mac_addr):
        self.mambo = Mambo(mac_addr, use_wifi=False)

        info("Trying to connect")
        success = self.mambo.connect(num_retries=3)
        info("Connected: %s" % success)

    def __del__ (self):
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
        duration, = tree.children
        print(duration)
        #duration = float(duration)
        
        #self.mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=10, duration=duration)
        self.mambo.smart_sleep(2)

    def down(self, tree):
        duration, = tree.children
        #duration = float(duration)
        
        #self.mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-10, duration=duration)
        self.mambo.smart_sleep(2)

    def move_in_steps(roll, pitch, yaw, v_m, duration):
        for _ in range(floor(duration)):
            self.mambo.fly_direct(roll, pitch, yaw, v_m, 1)
            self.mambo.smart_sleep(2)

        if floor(duration) is not duration:
            self.mambo.fly_direct(roll, pitch, yaw, v_m, duration - floor(duration))
            self.mambo.smart_sleep(2)

    
    def left(self, tree):
        duration, = tree.children
        duration = float(duration)

        self.move_in_steps(roll=-10,
                           pitch=0,
                           yaw=0,
                           v_m=0,
                           duration=duration)

    def right(self, tree):
        duration, = tree.children
        duration = float(duration)

        self.move_in_steps(roll=10,
                           pitch=0,
                           yaw=0,
                           v_m=0,
                           duration=duration)

    def forward(self, tree):
        duration, = tree.children
        print(duration)
        duration = float(duration)

        self.move_in_steps(roll=0,
                           pitch=10,
                           yaw=0,
                           v_m=0,
                           duration=duration)

    def backward(self, tree):
        duration, = tree.children
        duration = float(duration)

        self.move_in_steps(roll=0,
                           pitch=-10,
                           yaw=0,
                           v_m=0,
                           duration=duration)

    def rotatel(self, tree):
        degrees, = tree.children
        degrees = float(degrees)

        self.mambo.turn_degrees(-degrees)
        self.mambo.smart_sleep(3)

    def rotater(self, tree):
        degrees, = tree.children
        degrees = float(degrees)

        self.mambo.turn_degrees(degrees)
        self.mambo.smart_sleep(3)

    def wait(self, tree):
        seconds, = tree.children
        seconds = float(seconds)

        info('Waiting {} seconds'.format(seconds))
        self.mambo.smart_sleep(seconds)
