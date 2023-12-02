#!/usr/bin/env python3

import fileinput
import re
from functools import reduce
from operator import mul


def main():
    game_info = [line.strip() for line in fileinput.input()]

    color_max_count_dicts = [parse_line(line) for line in game_info]
    result = sum(
        get_min_cubes_needed_to_play(color_max_count_dict)
        for color_max_count_dict in color_max_count_dicts
    )
    print(result)


def parse_line(line):
    """
    From game info line, parse out the color of cubes and their max seen count.
    """
    regex = re.compile(r"(\d+) (\w+)")
    matches = re.findall(regex, line)

    color_max_count_dict = {}
    for count, color in matches:
        count = int(count)
        curr_max_cubes = color_max_count_dict.get(color, 0)
        color_max_count_dict[color] = max(count, curr_max_cubes)

    return color_max_count_dict


def get_min_cubes_needed_to_play(color_min_count_dict):
    """
    Get the minimum number of cubes needed to play the game.

    Multiply the min number of cubes needed for each color.
    """
    return reduce(mul, color_min_count_dict.values(), 1)


if __name__ == "__main__":
    main()
