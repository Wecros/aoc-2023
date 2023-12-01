#!/usr/bin/env python3

import fileinput


def main():
    lines = [line.strip() for line in fileinput.input()]
    result = sum([parse_line(line) for line in lines])
    print(result)


def parse_line(line):
    """
    Parse a line of text and return the first and last digit found
    merged together as an integer.
    """
    first_num = None
    last_num = None
    for char in line:
        try:
            int(char)
        except ValueError:
            continue
        if first_num is None:
            first_num = char
        else:
            last_num = char
    if first_num is None:
        raise ValueError("No numbers found in line")
    if last_num is None:
        last_num = first_num
    num_string = first_num + last_num
    return int(num_string)


if __name__ == "__main__":
    main()
