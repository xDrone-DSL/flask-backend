import antlr4

from antlr.xDroneLexer import xDroneLexer, CommonTokenStream
from antlr.xDroneParser import xDroneParser
from xdrone.visitors.compiler_utils.command import Command
from xdrone.visitors.compiler_utils.compile_error import XDroneSyntaxError
from xdrone.visitors.compiler_utils.error_listener import ParserErrorListener
from xdrone.visitors.compiler_utils.type_hints import NestedCommands
from xdrone.visitors.fly import Fly
from xdrone.visitors.interpreter import Interpreter
from xdrone.visitors.state_safety_checker.safety_checker import SafetyChecker
from xdrone.visitors.state_safety_checker.drone_config import DroneConfig, DefaultDroneConfig
from xdrone.visitors.state_safety_checker.safety_config import SafetyConfig, DefaultSafetyConfig
from xdrone.visitors.state_safety_checker.state_updater import StateUpdater
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


def generate_commands(program, symbol_table=None, function_table=None):
    input_stream = antlr4.InputStream(program)
    # lexing
    lexer = xDroneLexer(input_stream)
    stream = CommonTokenStream(lexer)
    # parsing
    parser = xDroneParser(stream)
    parser.removeErrorListeners()
    error_listener = ParserErrorListener()
    parser.addErrorListener(error_listener)
    tree = parser.prog()
    if error_listener.syntax_errors:
        raise XDroneSyntaxError(error_listener.get_error_string())

    state_updater = StateUpdater(DefaultDroneConfig())  # TODO: move to parameter
    commands, states = Interpreter(state_updater, symbol_table, function_table).visit(tree)
    check_safety = False  # TODO: move to parameter
    if check_safety:
        safety_checker = SafetyChecker(DefaultSafetyConfig())  # TODO: move to parameter
        safety_checker.check(commands, states)

    return commands


if __name__ == '__main__':
    commands = generate_commands(r"""
    main () {
        takeoff();
        wait(100);
    }
    """)
    for c in commands: print(c)
    drone_config = DroneConfig(speed_mps=0.5, rotate_speed_dps=45, takeoff_height_meters=1)
    safety_config = SafetyConfig(max_seconds=60, max_x_meters=2, max_y_meters=2, max_z_meters=2,
                                 min_x_meters=-2, min_y_meters=-2, min_z_meters=0)
