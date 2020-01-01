from logging import info
from lark import Visitor
from pyparrot.Minidrone import Mambo
from math import floor, pi, sin, cos, radians

TAKE_OFF_HEIGHT = 83
HORIZONTAL_CALIBRATION = 35
VERTICAl_CALIBRATION = 10



def toFloat(tree):
    return float(tree.children[0].children[0])

class Fly(Visitor):
    def __init__(self, mac_addr):
        self.mambo = Mambo(mac_addr, use_wifi=False)
        self.x = 0
        self.y = 0
        self.z = 90
        # Angle of drone from the x axis (east)
        self.theta = 0

        info("Trying to connect")
        success = self.mambo.connect(num_retries=3)
        info("Connected: %s" % success)

    def __del__ (self):
        info("Disconnecting")
        self.mambo.safe_land(5)
        self.mambo.disconnect()

    def takeoff(self, tree):
        info('Taking off')
        self.mambo.safe_takeoff(5)
        self.mambo.smart_sleep(1)

        self.z = TAKE_OFF_HEIGHT

    def land(self, tree):
        info('Landing')
        self.mambo.safe_land(5)

    def up(self, tree):
        duration = toFloat(tree)
        
        self.mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=10, duration=duration)
        self.mambo.smart_sleep(2)

        self.z += VERTICAL_CALIBRATION * duration

    def down(self, tree):
        duration = toFloat(tree)

        
        self.mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-10, duration=duration)
        self.mambo.smart_sleep(2)
        
        self.z -= VERTICAL_CALIBRATION * duration

    def move_in_steps(self, roll, pitch, yaw, v_m, duration):
        for _ in range(floor(duration)):
            self.mambo.fly_direct(roll, pitch, yaw, v_m, 1)
            self.mambo.smart_sleep(2)

        if floor(duration) is not duration:
            self.mambo.fly_direct(roll, pitch, yaw, v_m, duration - floor(duration))
            self.mambo.smart_sleep(2)

    
    def left(self, tree):
        duration = toFloat(tree)


        self.move_in_steps(roll=-10,
                           pitch=0,
                           yaw=0,
                           v_m=0,
                           duration=duration)
        self.x += duration * cos(radians(self.theta) + pi/2)
        self.y += duration * sin(radians(self.theta) + pi/2)


    def right(self, tree):
        duration = toFloat(tree)


        self.move_in_steps(roll=10,
                           pitch=0,
                           yaw=0,
                           v_m=0,
                           duration=duration)
        self.x += duration * cos(radians(self.theta) - pi/2)
        self.y += duration * sin(radians(self.theta) - pi/2)

    def forward(self, tree):
        duration = toFloat(tree)


        self.move_in_steps(roll=0,
                           pitch=10,
                           yaw=0,
                           v_m=0,
                           duration=duration)
        self.x += duration * cos(radians(self.theta))
        self.y += duration * sin(radians(self.theta))

    def backward(self, tree):
        duration = toFloat(tree)


        self.move_in_steps(roll=0,
                           pitch=-10,
                           yaw=0,
                           v_m=0,
                           duration=duration)
        self.x += duration * cos(radians(self.theta) + pi)
        self.y += duration * sin(radians(self.theta) + pi)

    def rotatel(self, tree):
        degrees = toFloat(tree)


        self.mambo.turn_degrees(-degrees)
        self.mambo.smart_sleep(3)
        self.theta += degrees

    def rotater(self, tree):
        degrees = toFloat(tree)


        self.mambo.turn_degrees(degrees)
        self.mambo.smart_sleep(3)
        self.theta -= degrees

    def wait(self, tree):
        duration = toFloat(tree)


        info('Waiting {} seconds'.format(duration))
        self.mambo.smart_sleep(duration)
    
    def abort(self):
        self.mambo.safe_land(5)
