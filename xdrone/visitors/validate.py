from logging import info
from lark import Visitor
from math import cos, sin, pi, radians


def toFloat(tree):
    return float(tree.children[0].children[0])


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
        self.max_x = max(self.max_x, self.x)
        self.max_y = max(self.max_y, self.y)

    def up(self, tree):
        duration = toFloat(tree)

        self.z += duration
        self.min_z = min(self.min_z, self.z)
        self.max_z = max(self.max_z, self.z)

    def down(self, tree):
        duration = toFloat(tree)

        self.z -= duration
        self.min_z = min(self.min_z, self.z)
        self.max_z = max(self.max_z, self.z)

    def left(self, tree):
        duration = toFloat(tree)

        self.travel(self.direction + pi/2, duration)

    def right(self, tree):
        duration = toFloat(tree)

        self.travel(self.direction - pi/2, duration)

    def forward(self, tree):
        duration = toFloat(tree)

        self.travel(self.direction, duration)

    def backward(self, tree):
        duration = toFloat(tree)

        self.travel(self.direction - pi, duration)

    def rotatel(self, tree):
        rads = radians(toFloat(tree))

        self.direction += rads

    def rotater(self, tree):
        rads = radians(toFloat(tree))

        self.direction -= rads
