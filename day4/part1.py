#!/usr/bin/env python3

import fileinput
import re


def main():
    card_lines = [line.strip() for line in fileinput.input()]
    total_points = 0
    for card in card_lines:
        total_points += parse_card(card)

    print(total_points)


def parse_card(card_line: str):
    """
    From cards, get one card line and parse it. Get the winning points for the card.

    On left they are winning numbers, separated by column "|" are my numbers on the right side.
    Numbers that match from both side are my winning points. First number is worth 1 point, every other number doubles the points.
    """
    card_points = 0
    match = re.search(r"Card +\d+:([\d ]+)\|([\d ]+)", card_line)
    winning_numbers = match.group(1).split()
    my_numbers = match.group(2).split()

    for number in winning_numbers:
        if number in my_numbers:
            card_points = 1 if not card_points else card_points * 2

    return card_points


if __name__ == "__main__":
    main()
