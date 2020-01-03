from logging import info
from lark import Transformer, Discard
from math import radians


def wrap_command(command, val):
    return {"action": command, "value": val}


class Simulate(Transformer):

    def __default__(self, command, children, meta):
        value = children[0]
        return wrap_command(command, value)

    def fly(self, children):
        return children

    def ignore_command(self, _):
        raise Discard()

    takeoff = land = action = ignore_command

    def number(self, value):
        # value is a singleton list containing the a token containing the
        # actual value
        return float(value[0])

    def rotatel(self, children):
        degrees, = children

        return wrap_command("rotateL", radians(degrees))

    def rotater(self, children):
        degrees, = children

        return wrap_command("rotateR", radians(degrees))
