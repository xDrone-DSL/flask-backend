import logging
from lark import Transformer, Discard
from math import radians


def wrap_command(command, *val):
    return {"action": command, "value": list(val)}


class Simulate(Transformer):

    # def __default__(self, command, children, meta):
    #     logging.error("Ignoring unsupported command %s with children %s" % (command, children))
    #     raise Discard()

    def fly(self, children):
        return children

    # def ignore_command(self, _):
    #     raise Discard()

    def takeoff(self, children):
        return wrap_command("takeoff")

    def land(self, children):
        return wrap_command("land")

    def up(self, children):
        value = children[0]
        return wrap_command("up", value)

    def down(self, children):
        value = children[0]
        return wrap_command("down", value)

    def left(self, children):
        value = children[0]
        return wrap_command("left", value)

    def right(self, children):
        value = children[0]
        return wrap_command("right", value)

    def forward(self, children):
        value = children[0]
        return wrap_command("forward", value)

    def backward(self, children):
        value = children[0]
        return wrap_command("backward", value)

    def rotatel(self, children):
        degrees, = children
        return wrap_command("rotateL", radians(degrees))

    def rotater(self, children):
        degrees, = children
        return wrap_command("rotateR", radians(degrees))

    def wait(self, children):
        value = children[0]
        return wrap_command("wait", value)

    def action(self, children):
        return wrap_command("action")

    def repeat(self, children):
        times = int(children[0])
        commands = children[1:]
        return commands * times

    def number(self, value):
        # value is a singleton list containing the a token containing the
        # actual value
        return float(value[0])

