#!/usr/bin/env python

import logging
from xdrone_parser import xdrone_parser
from fly_visitor import Fly

def fly_drone(program):
    parse_tree = xdrone_parser.parse(program)
    Fly().visit(parse_tree)

def main():
    logging.basicConfig(level=logging.INFO)
    while True:
        code = input('> ')
        try:
            fly_drone(code)
        except Exception as e:
            logging.error(e)

if __name__ == '__main__':
    main()
