#!/usr/bin/env python

import logging
from xdrone import generate_simulation_json

def main():
    logging.basicConfig(level=logging.INFO)
    while True:
        code = input('> ')
        try:
            print(generate_simulation_json(code))
        except Exception as e:
            logging.error(e)

if __name__ == '__main__':
    main()
