#!/usr/bin/env python3

import fileinput
import re


def main():
    setup_map: dict = parse_input()
    seeds: list = setup_map["seeds"]
    map_keys = setup_map.keys() - {"seeds"}
    maps = {k: setup_map[k] for k in map_keys}

    # Compute the soil for seed
    last_map_category = "seed"
    location_numbers = []
    for seed in seeds:
        src = seed
        dest = None
        while last_map_category != "location":
            # get correct map based on last map category
            for tup in map_keys:
                if tup[0] == last_map_category:
                    needed_map = maps[tup]
                    last_map_category = tup[1]
                    break

            dest = calculate_dest(src, needed_map)
            src = dest

        location_numbers.append(dest)
        last_map_category = "seed"

    min_location = min(location_numbers)
    print(min_location)


def parse_input() -> dict[str, dict]:
    """
    Parse the input into a dict of dicts.

    Seeds are the first line, it's just a list of numbers.
    Then they are several mapping categories.
    Each line within a map contains three numbers.
    """

    text_input = "".join(fileinput.input())
    pattern = r"(?:seeds: .*\n+)|(?:\w+-to-\w+ map:\n[\d \n]*)"
    matches = re.findall(pattern, text_input, re.MULTILINE)

    input_map: dict = {}
    input_map["seeds"] = [int(num) for num in re.findall(r"\d+", matches[0])]

    for match in matches[1:]:
        all_numbers = [int(num) for num in re.findall(r"\d+", match)]
        # split the numbers into groups of 3
        numbers_in_groups = tuple(tuple(all_numbers[i : i + 3]) for i in range(0, len(all_numbers), 3))
        split_map_name = tuple(match.split(" map:")[0].split("-to-"))
        input_map[split_map_name] = numbers_in_groups

    return input_map


def calculate_dest(src: int, map_data: tuple[tuple[int, int, int]]) -> int:
    """
    map_data is a tuple of tuples of 3 numbers.

    Numbers have this meaning:
     - 1st: the destination range start
     - 2nd: the source range start
     - 3rd: the range length.

    Compute the correctly returned dest val based on src val, if it exists in the map. Otherwise, return src.
    """
    for group in map_data:
        dest_start, src_start, map_range = group
        if src_start <= src < src_start + map_range:
            return dest_start + (src - src_start)
    return src


if __name__ == "__main__":
    main()
