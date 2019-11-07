#!/usr/bin/env python

import logging
from xdrone import fly, validate

def main():
    logging.basicConfig(level=logging.INFO)
    while True:
        code = input('> ')
        try:
            mambo_addr = "d0:3a:86:9d:e6:5a"
            validate(code)
            # fly(code, mambo_addr)
        except Exception as e:
            logging.error(e)

if __name__ == '__main__':
    main()
