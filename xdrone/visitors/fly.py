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
    def __init__(self, mac_addr, rs):
        self.mambo = Mambo(mac_addr, use_wifi=False)
        self.requirements = rs

        # positive is east
        self.x = 0
        # positive is up
        self.y = 0
        # positive is south
        self.z = 0
        # Angle of drone from the x axis, so starts north
        self.theta = 90

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

        for r in self.requirements:
            r.update_on_land(self.x, self.y, self.z)

    def up(self, tree):
        duration = toFloat(tree)
        
        self.mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=10, duration=duration)
        self.mambo.smart_sleep(2)

        self.y += VERTICAL_CALIBRATION * duration

    def down(self, tree):
        duration = toFloat(tree)
        
        self.mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-10, duration=duration)
        self.mambo.smart_sleep(2)
        
        self.y -= VERTICAL_CALIBRATION * duration

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
        self.x += HORIZONTAL_CALIBRATION * duration * cos(radians(self.theta) + pi/2)
        self.z -= HORIZONTAL_CALIBRATION * duration * sin(radians(self.theta) + pi/2)

        for r in self.requirements:
            r.update_on_move(self.x, self.y, self.z)

    def right(self, tree):
        duration = toFloat(tree)
        self.move_in_steps(roll=10,
                           pitch=0,
                           yaw=0,
                           v_m=0,
                           duration=duration)
        self.x += HORIZONTAL_CALIBRATION * duration * cos(radians(self.theta) - pi/2)
        self.z -= HORIZONTAL_CALIBRATION * duration * sin(radians(self.theta) - pi/2)

        for r in self.requirements:
            r.update_on_move(self.x, self.y, self.z)

    def forward(self, tree):
        duration = toFloat(tree)
        self.move_in_steps(roll=0,
                           pitch=10,
                           yaw=0,
                           v_m=0,
                           duration=duration)
        self.x += HORIZONTAL_CALIBRATION * duration * cos(radians(self.theta))
        self.z -= HORIZONTAL_CALIBRATION * duration * sin(radians(self.theta))

        for r in self.requirements:
            r.update_on_move(self.x, self.y, self.z)

    def backward(self, tree):
        duration = toFloat(tree)
        self.move_in_steps(roll=0,
                           pitch=-10,
                           yaw=0,
                           v_m=0,
                           duration=duration)
        self.x += HORIZONTAL_CALIBRATION * duration * cos(radians(self.theta) + pi)
        self.z -= HORIZONTAL_CALIBRATION * duration * sin(radians(self.theta) + pi)

        for r in self.requirements:
            r.update_on_move(self.x, self.y, self.z)

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

    def action(self, tree):
        self.mambo.smart_sleep(2)
        info('Performed action at ({}, {}, {})'.format(self.x, self.y, self.z))
        for r in self.requirements:
            r.update_on_action(self.x, self.y, self.z)

    def abort(self):
        self.mambo.safe_land(5)
