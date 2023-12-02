#!/usr/bin/env python3

import fileinput
import re


def main():
    game_info = [line.strip() for line in fileinput.input()]
    elf_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    result = 0
    color_max_count_dicts = [parse_line(line) for line in game_info]
    for i, color_max_count_dict in enumerate(color_max_count_dicts):
        if can_game_be_played(color_max_count_dict, elf_cubes.items()):
            result += i + 1
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


def can_game_be_played(color_max_count_dict, elf_cubes):
    """
    From elf cubes and current game, determine if game can be played.
    """
    for color, max_count in elf_cubes:
        if color in color_max_count_dict:
            if color_max_count_dict[color] > max_count:
                return False
    return True


if __name__ == "__main__":
    main()
