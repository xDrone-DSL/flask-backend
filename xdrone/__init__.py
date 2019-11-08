from xdrone.parser import xdrone_parser
from xdrone.visitors.fly import Fly
from xdrone.visitors.simulate import Simulate
from xdrone.visitors.validate import Validate

def fly(program, addr = "d0:3a:86:9d:e6:5a"):
    parse_tree = xdrone_parser.parse(program)
    Fly(addr).visit(parse_tree)

def validate(program):
    parse_tree = xdrone_parser.parse(program)
    Validate().visit(parse_tree)

def gen_simulate_commands(program):
    parse_tree = xdrone_parser.parse(program)
    return Simulate().transform(parse_tree)
