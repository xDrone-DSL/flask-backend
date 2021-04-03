from typing import Union, List

from xdrone import Command

NestedCommands = Union[Command, List['NestedCommands']]