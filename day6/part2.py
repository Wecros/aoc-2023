#!/usr/bin/env python3

import fileinput
import re


def main():
    time, distance = parse_input()
    sum_wins = get_possible_winning_buttons(time, distance)
    print(sum_wins)


def parse_input():
    lines = [line.strip() for line in fileinput.input()]
    times_str = re.findall(r"\d+", lines[0])
    distances_str = re.findall(r"\d+", lines[1])
    time = int("".join(times_str))
    distance = int("".join(distances_str))
    return time, distance


def get_possible_winning_buttons(time, distance_to_beat):
    """
    From time and distance, get the possible winning buttons.

    Your boat has a button, it can be only held at the start of the race.
    The number of milliseconds you hold the button the velocity of millimeters per second your boat will have.
    But the time spent holding the button will be subtracted from the total time left in the race.

    They are more possible ways to win, get all of them.
    """
    possible_ways_to_win = 0
    for button_press in range(0, time):
        time_left = time - button_press
        velocity = button_press
        distance_traveled = velocity * time_left
        if distance_traveled > distance_to_beat:
            possible_ways_to_win += 1
    return possible_ways_to_win


if __name__ == "__main__":
    main()
