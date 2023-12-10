#!/usr/bin/env python3

import fileinput
from collections import deque
import copy


def main():
    computed_maze = parse_input()
    # get largest number from computed maze = farthest distance from animal
    flattened_maze = [item for sublist in computed_maze for item in sublist]
    max_distance = max(flattened_maze)
    print(max_distance)


def parse_input():
    """
    Description:
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

    Example maze:
    .....
    .S-7.
    .|.|.
    .L-J.
    .....

    More complex maze:
    ..F7.
    .FJ|.
    SJ.L7
    |F--J
    LJ...

    Most complex maze:
    7-F7-
    .FJ|7
    SJLL7
    |F--J
    LJ.LJ

    From this input we need to create a possible maze starting from S.
    It should be 2D list, possible path will be denoted as "1", not possible as "0".
    Not possible is empty spaces or pipes which are not connected to the main path (from S).
    """

    input = [line.strip() for line in fileinput.input()]
    input = [list(line) for line in input]

    north = (-1, 0)
    south = (1, 0)
    east = (0, 1)
    west = (0, -1)

    pipe_direction_map = {
        "|": [north, south],
        "-": [east, west],
        "L": [north, east],
        "J": [north, west],
        "7": [south, west],
        "F": [south, east],
        ".": [],
        "S": [north, east, south, west],
    }

    # first find S
    start_row = 0
    start_col = 0
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] == "S":
                start_row = row
                start_col = col
                break

    # now do bfs
    visited = set()
    queue = deque([((start_row, start_col), 0)])
    output = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]

    while queue:
        node, curr_distance = queue.popleft()
        if node in visited:
            continue

        visited.add(node)

        row = node[0]
        col = node[1]
        curr_tile = input[row][col]
        output[row][col] = curr_distance

        for direction in pipe_direction_map[curr_tile]:
            new_row = row + direction[0]
            new_col = col + direction[1]
            # check if out of bounds
            if new_row < 0 or new_row >= len(input) or new_col < 0 or new_col >= len(input[0]):
                continue

            neighbor_node = (new_row, new_col)
            if neighbor_node in visited:
                continue

            coming_from = tuple(num * -1 for num in direction)
            next_tile = input[new_row][new_col]
            match next_tile:
                case ".":
                    continue
                case "|":
                    if not (coming_from == north or coming_from == south):
                        continue
                case "-":
                    if not (coming_from == east or coming_from == west):
                        continue
                case "L":
                    if not (coming_from == north or coming_from == east):
                        continue
                case "J":
                    if not (coming_from == north or coming_from == west):
                        continue
                case "7":
                    if not (coming_from == south or coming_from == west):
                        continue
                case "F":
                    if not (coming_from == south or coming_from == east):
                        continue

            neighbor = (neighbor_node, curr_distance + 1)
            queue.append(neighbor)

    # for line in output:
    #     for char in line:
    #         print(char, end=' ')
    #     print()

    return output


if __name__ == "__main__":
    main()
