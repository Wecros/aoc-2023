#!/usr/bin/env python3

"""
As a solution to the part 2, I just optimized what I could and ran the solution in pypy.
After about 23 minutes, I got the result.
"""

import fileinput
import re


def main():
    setup_map = parse_input()
    seeds = setup_map["seeds"]
    map_keys = list(setup_map.keys())
    map_keys.remove("seeds")
    maps = {k: setup_map[k] for k in map_keys}

    seed_ranges = convert_seeds_to_ranges(seeds)
    map_lookup = {src_cat: maps[(src_cat, dest_cat)] for src_cat, dest_cat in map_keys}

    categories = get_categories_in_order(map_keys)
    categories.remove("location")

    curr_lowest_location = float("inf")

    for seed_range in seed_ranges:
        for seed in seed_range:
            src = seed
            dest = None
            for category in categories:
                needed_map = map_lookup[category]
                dest = calculate_dest(src, needed_map)
                src = dest
            curr_lowest_location = min(curr_lowest_location, dest)

    print(curr_lowest_location)


def calculate_dest(src, map_data):
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
        if src_start <= src < (src_start + map_range):
            return dest_start + (src - src_start)
    return src


def convert_seeds_to_ranges(seeds):
    """
    Sort the ranges by start, then convert to range objects.

    No need for overlap optimization, since there is no overlap in the input.
    """
    start_end_ranges = [(start, start + range_) for start, range_ in seeds]
    start_end_ranges.sort()
    ranges = [range(start, end) for start, end in start_end_ranges]
    return ranges


def get_categories_in_order(map_keys):
    """Get the order of the categories from the input maps, starting from 'seed'."""
    categories_order = ["seed"]
    last_category = "seed"
    while last_category != "location":
        for tup in map_keys:
            if tup[0] == last_category:
                last_category = tup[1]
                categories_order.append(last_category)
                break
    return categories_order


def parse_input():
    """
    Parse the input into a dict of dicts.

    Seeds are the first line, it's just a list of numbers.

    Then they are several mapping categories.
    Each line within a map contains three numbers.
    """
    input_map = {}
    text_input = "".join(fileinput.input())
    pattern = r"(?:seeds: .*\n+)|(?:\w+-to-\w+ map:\n[\d \n]*)"
    matches = re.findall(pattern, text_input, re.MULTILINE)

    seeds = [int(num) for num in re.findall(r"\d+", matches[0])]
    # split the seeds into tuples of 2
    input_map["seeds"] = tuple(tuple(seeds[i : i + 2]) for i in range(0, len(seeds), 2))

    for match in matches[1:]:
        all_numbers = [int(num) for num in re.findall(r"\d+", match)]
        # split the numbers into groups of 3
        numbers_in_groups = tuple(tuple(all_numbers[i : i + 3]) for i in range(0, len(all_numbers), 3))
        split_map_name = tuple(match.split(" map:")[0].split("-to-"))
        input_map[split_map_name] = numbers_in_groups

    return input_map


if __name__ == "__main__":
    main()
