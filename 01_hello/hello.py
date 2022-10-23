#!/usr/bin/env python3
"""
Say hello
"""
from argparse import ArgumentParser, Namespace


def get_args() -> Namespace:
    """Get the command-line arguments"""

    parser: ArgumentParser = ArgumentParser(description='Say hello')

    # parser.add_argument('name', help='Name to greet') # 1. positional argument
    parser.add_argument('-n', '--name', metavar='name', default='World', help='name to greet')   # 2. optional argument

    return parser.parse_args()


def main():
    """main"""

    args: Namespace = get_args()

    # print(f'args: {args}') # Namespace(name='horse')
    print('Hello, ' + args.name + '!')

    # The argparse module also automatically:
    # - generates help and usage messages
    # - issues errors when users give the program invalid arguments


if __name__ == '__main__':  # guard from auto-executing, when the script is not main and is instead imported to a main script
    main()
