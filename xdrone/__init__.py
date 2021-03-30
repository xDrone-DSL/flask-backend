from typing import Union, List

from lark.exceptions import VisitError

from requirements import generate_requirements
from xdrone.parser import xdrone_parser
from xdrone.visitors.compiler_utils.command import Command
from xdrone.visitors.fly import Fly
from xdrone.visitors.interpreter import Interpreter
from xdrone.visitors.validate import Validate


def fly(program, rs, addr="d0:3a:86:9d:e6:5a"):
    parse_tree = xdrone_parser.parse(program)
    requirements = generate_requirements(rs)
    Fly(addr, requirements).visit(parse_tree)

    return all(r.is_completed() for r in requirements)


def validate(program, bounds):
    parse_tree = xdrone_parser.parse(program)
    validator = Validate()
    validator.visit(parse_tree)

    if validator.max_z > bounds["height"]:
        return {"success": False, "message": "The drone flies too high"}
    if (
        abs(validator.max_x) > bounds["width"] / 2 or
        abs(validator.min_x) > bounds["width"] / 2 or
        abs(validator.max_y) > bounds["depth"] / 2 or
        abs(validator.min_y) > bounds["depth"] / 2
    ):
        return {"success": False, "message": "The drone flies out of bounds"}

    return {"success": True}


def generate_simulation_json(program):
    commands = generate_commands(program)
    return [command.to_simulation_json() for command in commands]


def generate_commands(program, symbol_table=None):
    NestedCommands = Union[Command, List['NestedCommands']]
    def _flatten(commands: NestedCommands) -> List[Command]:
        if isinstance(commands, list):
            return [a for i in commands for a in _flatten(i)]
        else:
            return [commands]

    parse_tree = xdrone_parser.parse(program)
    try:
        return _flatten(Interpreter(symbol_table).transform(parse_tree))
    except VisitError as e:
        raise e.orig_exc
