#!/usr/bin/env python3

import fileinput
import re


def main():
    instructions, graph = parse_input()

    start_node = "AAA"
    curr_node = start_node
    final_node = "ZZZ"
    instruction_counter = 0
    while curr_node != final_node:
        curr_instruction = instructions[instruction_counter % len(instructions)]
        curr_node = graph[curr_node][curr_instruction]
        instruction_counter += 1

    print(instruction_counter)


def parse_input():
    """
    Create graph based on this input.
    RL are the instructions. Convert L to 0 and R to 1 indexes.

    ```
    RL

    AAA = (BBB, CCC)
    BBB = (DDD, EEE)
    CCC = (ZZZ, GGG)
    DDD = (DDD, DDD)
    EEE = (EEE, EEE)
    GGG = (GGG, GGG)
    ZZZ = (ZZZ, ZZZ)
    ```
    """
    # get the whole fileinput as a string
    input_string = "".join(fileinput.input())
    groups = input_string.split("\n\n")
    graph_instructions = re.findall(r"(\w+) = \((\w+), (\w+)\)", groups[1])

    graph = {}
    for instruction in graph_instructions:
        node = instruction[0]
        neighbors = [instruction[1], instruction[2]]
        graph[node] = neighbors

    instructions = [1 if instruction == "R" else 0 for instruction in groups[0]]
    return instructions, graph


if __name__ == "__main__":
    main()
