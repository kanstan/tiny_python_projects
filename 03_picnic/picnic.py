#!/usr/bin/env python3
"""
Lists the food items you bring to a picnic
"""
from argparse import ArgumentParser, Namespace
from typing import List


def get_command_line_args() -> Namespace:
    parser: ArgumentParser = ArgumentParser(description='Lists the food items you bring to a picnic')
    parser.add_argument('food', 
                        nargs='+', # 1+ arguments expected -> gathered into a list
                        help='Food items to bring to a picnic')
    
    parser.add_argument('-s', '--sorted', 
                        action='store_true', # action='store_true' implies default=False
                        help='Sort the items (default: False)') 

    return parser.parse_args()


def format_list(list: List[str]) -> str:
    if(len(list) == 0):
        return ""
    elif(len(list) == 1):
        return list[0]
    elif(len(list) == 2):
        return " and ".join(list)
    else:
        return ", ".join(list[:-1]) + ", and " + list[-1]


def main() -> None:
    args: Namespace = get_command_line_args()
    foods: List[str] = args.food

    if(args.sorted):
        # sorted(original_list) - returns (new) sorted list, original_list stays unmodified, works for any iterable
        # original_list.sort() - returns None, modifies original_list, works only for lists, slightly more efficient than sorted()
        foods.sort(key=str.lower) # sorts alphabetically, ignores upper/lower case (key=str.lower)

    foodsFormatted: str = format_list(foods)
    print(f'You are bringing {foodsFormatted}.')


if __name__ == '__main__':
    main()
