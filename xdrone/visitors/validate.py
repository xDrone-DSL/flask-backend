from logging import info
from lark import Visitor
from math import cos, sin, pi, radians


class Validate(Visitor):

    def __init__(self):
        self.direction = 0
        self.x, self.y, self.z = 0, 0, 0
        self.min_x, self.min_y, self.min_z = 0, 0, 0
        self.max_x, self.max_y, self.max_z = 0, 0, 0

    def travel(self, angle, duration):
        self.x -= duration * sin(angle)
        self.y += duration * cos(angle)
        self.min_x = min(self.min_x, self.x)
        self.min_y = min(self.min_y, self.y)
        self.min_z = min(self.min_z, self.z)
        self.max_x = max(self.max_x, self.x)
        self.max_y = max(self.max_y, self.y)
        self.max_z = max(self.max_z, self.z)

    def up(self, tree):
        duration, = tree.children
        duration = float(duration)

        self.z += duration

    def down(self, tree):
        duration, = tree.children
        duration = float(duration)

        self.z -= duration

    def left(self, tree):
        duration, = tree.children
        duration = float(duration)

        self.travel(self.direction + pi/2, duration)

    def right(self, tree):
        duration, = tree.children
        duration = float(duration)

        self.travel(self.direction - pi/2, duration)

    def forward(self, tree):
        duration, = tree.children
        duration = float(duration)

        self.travel(self.direction, duration)

    def backward(self, tree):
        duration, = tree.children
        duration = float(duration)

        self.travel(self.direction - pi, duration)

    def rotatel(self, tree):
        degrees, = tree.children
        rads = radians(float(degrees))

        self.direction += rads

    def rotater(self, tree):
        degrees, = tree.children
        rads = radians(float(degrees))

        self.direction -= rads
