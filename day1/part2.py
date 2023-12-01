#!/usr/bin/env python3

import fileinput


def main():
    lines = [line.strip() for line in fileinput.input()]

    result = 0
    for line in lines:
        string_indexes_digits_map = get_indexes_values_for_string_digits(line)
        num_indexes_digits_map = get_indexes_values_for_num_digits(line)
        final_indexes_digits_map = {
            **string_indexes_digits_map,
            **num_indexes_digits_map,
        }
        min_idx = min(final_indexes_digits_map.keys())
        max_idx = max(final_indexes_digits_map.keys())
        first_digit = final_indexes_digits_map[min_idx]
        last_digit = final_indexes_digits_map[max_idx]
        number = int(first_digit + last_digit)
        result += number

    print(result)


def get_indexes_values_for_string_digits(line):
    def find_all_substr_indexes(line, substr):
        start = 0
        while True:
            start = line.find(substr, start)
            if start == -1:
                return
            yield start
            start += len(substr)

    string_digits_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    indexes_digits_map = {}

    for string, val in string_digits_map.items():
        idxs = find_all_substr_indexes(line, string)
        for idx in idxs:
            indexes_digits_map[idx] = val
    return indexes_digits_map


def get_indexes_values_for_num_digits(line):
    indexes_digits_map = {}

    for idx, char in enumerate(line):
        try:
            int(char)
        except ValueError:
            continue
        indexes_digits_map[idx] = char

    return indexes_digits_map


if __name__ == "__main__":
    main()
