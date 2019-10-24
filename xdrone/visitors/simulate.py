from logging import info
from lark import Visitor

class Simulate(Visitor):
    def __init__(self):
        self.commands = []

    def add_command(self, command, val):
        self.commands.append({action: command, value: val})

    def takeoff(self, tree):
        self.add_command("up", 2.5)

    def land(self, tree):
        self.add_command("down", 2.5)

    def up(self, tree):
        duration, = tree.children
        duration = int(duration)

        self.add_command("up", duration)

    def down(self, tree):
        duration, = tree.children
        duration = int(duration)

        self.add_command("down", duration)

    def left(self, tree):
        duration, = tree.children
        duration = int(duration)

        self.add_command("left", duration)

    def right(self, tree):
        duration, = tree.children
        duration = int(duration)

        self.add_command("right", duration)

    def forward(self, tree):
        duration, = tree.children
        duration = int(duration)

        self.add_command("forward", duration)

    def backward(self, tree):
        duration, = tree.children
        duration = int(duration)

        self.add_command("backwards", duration)

    def rotatel(self, tree):
        duration, = tree.children
        duration = int(duration)

        self.add_command("up", duration)

    def rotater(self, tree):
        duration, = tree.children
        duration = int(duration)

        self.add_command("up", duration)

    def wait(self, tree):
        duration, = tree.children
        duration = int(duration)

        self.add_command("up", duration)
