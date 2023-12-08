#!/usr/bin/env python3

import fileinput
import re
import math


def main():
    engine_rows = [line.strip() for line in fileinput.input()]
    default_row = ["." for _ in range(len(engine_rows[0]))]
    total_engine_sum = 0
    for i, row in enumerate(engine_rows):
        previous_row = engine_rows[i - 1] if i > 0 else default_row.copy()
        next_row = engine_rows[i + 1] if i < len(engine_rows) - 1 else default_row.copy()
        total_engine_sum += parse_engine_row(i, row, previous_row, next_row)

    print(total_engine_sum)


def parse_engine_row(index, row, previous_row, next_row):
    """
    From engine, get this row, next row, and previous row.

    Find asterisks, get their indexes, and look around for numbers below, above, diagonally, and left/right.
    If there are exactly two numbers adjacent to the asterisk, multiply them together and add to the total.
    The numbers might be longer than one digit, so looking past asterisk's immediate neighbors is necessary.
    """
    number_sum_found_in_row = 0
    num_matches_in_row = re.finditer(r"\*", row)

    for match in num_matches_in_row:
        asterisk_index = match.start()
        look_start = asterisk_index - 1
        look_end = asterisk_index + 1
        if asterisk_index == 0:
            look_start = 0
        elif asterisk_index == len(row):
            look_end = len(row) - 1

        above_adj = get_adjacent_numbers_in_row(previous_row, look_start, look_end)
        left_right_adj = get_adjacent_numbers_in_row(row, look_start, look_end)
        below_adj = get_adjacent_numbers_in_row(next_row, look_start, look_end)
        adjacent_numbers = above_adj + left_right_adj + below_adj

        if len(adjacent_numbers) == 2:
            number_sum_found_in_row += math.prod(adjacent_numbers)

    return number_sum_found_in_row


def get_adjacent_numbers_in_row(row, look_start, look_end):
    adjacent_numbers = []
    numbers_in_above = re.finditer(r"\d+", row)
    for match in numbers_in_above:
        num_start = match.start()
        num_end = match.end() - 1
        num = int(match.group())
        # check for overlap
        if max(num_start, look_start) <= min(num_end, look_end):
            adjacent_numbers.append(num)
    return adjacent_numbers


if __name__ == "__main__":
    main()
