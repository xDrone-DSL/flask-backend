#!/usr/bin/env python

import logging
from xdrone import gen_simulate_commands

def main():
    logging.basicConfig(level=logging.INFO)
    while True:
        code = input('> ')
        try:
            print(gen_simulate_commands(code))
        except Exception as e:
            logging.error(e)

if __name__ == '__main__':
    main()
