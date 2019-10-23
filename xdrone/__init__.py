from xdrone.parser import xdrone_parser
from xdrone.visitors.fly import Fly

def fly(program, addr):
    parse_tree = xdrone_parser.parse(program)
    Fly(addr).visit(parse_tree)
