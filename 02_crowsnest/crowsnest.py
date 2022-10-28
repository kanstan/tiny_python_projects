#!/usr/bin/env python3
"""
Announces the appearance of something "off the larboard bow" to the captain of the ship
"""
from argparse import ArgumentParser, Namespace
from typing import Final, Tuple


def get_args() -> Namespace:
    """Get the command-line arguments"""

    parser: ArgumentParser = ArgumentParser(description='Announces the appearance')
    parser.add_argument('something', metavar='something', help='Something off the larboard bow')
    return parser.parse_args()


def main() -> None:
    args: Namespace = get_args()
    something: str = args.something
    article: str = select_article_for_word(something)
    print(f"Ahoy, Captain, {article} {something} off the larboard bow!")


def select_article_for_word(word: str) -> str:
    """Return correct indefinite article (a or an) for a given word """

    vowels: Final[Tuple[str, ...]] = ("a", "e", "i", "o", "u")
    if word[0].lower() in vowels:
        return "an"
    else:
        return "a"
    

if __name__ == '__main__': 
    main()