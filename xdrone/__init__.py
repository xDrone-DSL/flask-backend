from xdrone.parser import xdrone_parser
from xdrone.visitors.fly import Fly
from xdrone.visitors.simulate import Simulate
from xdrone.visitors.validate import Validate


def fly(program, addr="d0:3a:86:9d:e6:5a"):
    parse_tree = xdrone_parser.parse(program)
    Fly(addr).visit(parse_tree)


def validate(program, bounds):
    parse_tree = xdrone_parser.parse(program)
    validator = Validate()
    validator.visit(parse_tree)

    if validator.max_z > bounds["height"]:
        return {"sucess": False, "message": "The drone flies too high"}
    if (
        abs(validator.max_x) > bounds["width"] / 2 or
        abs(validator.min_x) > bounds["width"] / 2 or
        abs(validator.max_y) > bounds["depth"] / 2 or
        abs(validator.min_y) > bounds["depth"] / 2
    ):
        return {"sucess": False, "message": "The drone flies out of bounds"}

    return {"sucess": True}


def gen_simulate_commands(program):
    parse_tree = xdrone_parser.parse(program)
    return Simulate().transform(parse_tree)
