#!/usr/bin/env python3

import fileinput
import re


def main():
    card_lines = [line.strip() for line in fileinput.input()]
    card_points: dict = {}
    for i, card in enumerate(card_lines):
        card_points[i + 1] = parse_card(card)

    card_copies: dict = {k: 1 for k in range(1, len(card_points) + 1)}
    # Compute each card sequentially, add copies to the next cards.
    for i in range(1, len(card_points) + 1):
        curr_card_points = card_points[i]
        curr_card_copies = card_copies[i]
        # Add copies to the next cards.
        for j in range(1, curr_card_points + 1):
            # Multiply the copies by curr card copies.
            card_copies[i + j] += 1 * curr_card_copies

    total_scratchcards = sum(card_copies.values())
    print(total_scratchcards)


def parse_card(card_line: str):
    """
    From cards, get one card line and parse it. Get the total winning points out of mine.
    """
    points = 0
    match = re.search(r"Card +\d+:([\d ]+)\|([\d ]+)", card_line)
    winning_numbers = match.group(1).split()
    my_numbers = match.group(2).split()

    for number in winning_numbers:
        if number in my_numbers:
            points += 1

    return points


if __name__ == "__main__":
    main()
