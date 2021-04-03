from typing import List

import antlr4

from antlr.xDroneLexer import xDroneLexer, CommonTokenStream
from antlr.xDroneParser import xDroneParser
from xdrone.visitors.compiler_utils.command import Command
from xdrone.visitors.compiler_utils.type_hints import NestedCommands
from xdrone.visitors.fly import Fly
from xdrone.visitors.interpreter import Interpreter
from xdrone.visitors.validate import Validate


def fly(program, rs, addr="d0:3a:86:9d:e6:5a"):
    # TODO
    pass
    # parse_tree = xdrone_parser.parse(program)
    # requirements = generate_requirements(rs)
    # Fly(addr, requirements).visit(parse_tree)
    #
    # return all(r.is_completed() for r in requirements)


def validate(program, bounds):
    # TODO
    pass
    # parse_tree = xdrone_parser.parse(program)
    # validator = Validate()
    # validator.visit(parse_tree)
    #
    # if validator.max_z > bounds["height"]:
    #     return {"success": False, "message": "The drone flies too high"}
    # if (
    #     abs(validator.max_x) > bounds["width"] / 2 or
    #     abs(validator.min_x) > bounds["width"] / 2 or
    #     abs(validator.max_y) > bounds["depth"] / 2 or
    #     abs(validator.min_y) > bounds["depth"] / 2
    # ):
    #     return {"success": False, "message": "The drone flies out of bounds"}
    #
    # return {"success": True}


def generate_simulation_json(program):
    commands = generate_commands(program)
    return [command.to_simulation_json() for command in commands]


def generate_commands(program, symbol_table=None):
    def _flatten(commands: NestedCommands) -> List[Command]:
        if isinstance(commands, list):
            return [a for i in commands for a in _flatten(i)]
        else:
            return [commands]

    inputStream = antlr4.InputStream(program)
    # lexing
    lexer = xDroneLexer(inputStream)
    stream = CommonTokenStream(lexer)
    # parsing
    parser = xDroneParser(stream)
    tree = parser.prog()

    return _flatten(Interpreter(symbol_table).visit(tree))
