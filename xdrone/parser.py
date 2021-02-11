from lark import Lark
from os import path

grammar_path = path.join(path.dirname(__file__), "xdrone.lark")
xdrone_parser = Lark(open(grammar_path), start='prog')
