#!/usr/bin/env python3

"""
Incomplete solution. The solution works fine for the test input, but it is too computation heavy for
the real input. There needs to be some optimization in way of transitioning the graph without getting
the same nodes over and over again. Some cycle skipping or something like that.
"""

import fileinput
import re


def main():
    instructions, graph = parse_input()

    # start node is a node that ends with "A"
    start_nodes = tuple(node for node in graph.keys() if node.endswith("A"))
    curr_nodes = start_nodes
    instruction_counter = 0

    while not all(node.endswith("Z") for node in curr_nodes):
        curr_instruction = instructions[instruction_counter % len(instructions)]
        curr_nodes = [graph[node][curr_instruction] for node in curr_nodes]
        instruction_counter += 1

        if instruction_counter % 10000000 == 0:
            print(instruction_counter)

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


instructions, graph = parse_input()

if __name__ == "__main__":
    main()
