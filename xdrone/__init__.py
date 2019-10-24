from xdrone.parser import xdrone_parser
from xdrone.visitors.fly import Fly
from xdrone.visitors.simulate import Simulate

def fly(program, addr = "d0:3a:86:9d:e6:5a"):
    parse_tree = xdrone_parser.parse(program)
    Fly(addr).visit(parse_tree)

def gen_simulate_commands(program):
    parse_tree = xdrone_parser.parse(program)
    simulator = Simulate()
    simulator.visit(parse_tree)
    return simulator.commands
