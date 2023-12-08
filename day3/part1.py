#!/usr/bin/env python3

import fileinput
import re


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

    Find numbers, get their indexes, and look around the indexes below, above, diagonally, and left/right.
    """
    number_sum_found_in_row = 0
    num_matches_in_row = re.finditer(r"\d+", row)

    for match in num_matches_in_row:
        is_number_adjacent = False
        number_start = match.start()
        number_end = match.end()
        number = match.group()
        if number_start == 0:
            number_start = 1
        if number_end == len(row):
            number_end = len(row) - 1

        # check left/right
        if is_tile_symbol(row[number_start - 1]) or is_tile_symbol(row[number_end]):
            is_number_adjacent = True
        # check above + diagonals
        for i in range(number_start - 1, number_end + 1):
            if is_tile_symbol(previous_row[i]):
                is_number_adjacent = True
        # check below + diagonals
        for i in range(number_start - 1, number_end + 1):
            if is_tile_symbol(next_row[i]):
                is_number_adjacent = True

        if is_number_adjacent:
            number_sum_found_in_row += int(number)

    return number_sum_found_in_row


def is_tile_symbol(symbol):
    """symbol is not a number and not a dot"""
    return (not symbol.isdigit()) and (symbol != ".")


if __name__ == "__main__":
    main()
