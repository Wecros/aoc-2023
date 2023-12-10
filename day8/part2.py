#!/usr/bin/env python3

"""
~Incomplete solution. The solution works fine for the test input, but it is too computation heavy for
the real input. There needs to be some optimization in way of transitioning the graph without getting
the same nodes over and over again. Some cycle skipping or something like that.~

^ scratch this, by looking at the inputs more clearly and finding a little help on reddit,
the trick is that the start-end nodes are always the same and they cycle. So the solution is to
find the cycle length of each start node, and then find the least common multiple of all the cycle lengths.
"""

import fileinput
import re
import math


def main():
    instructions, graph = parse_input()

    # start node is a node that ends with "A"
    start_nodes = tuple(node for node in graph.keys() if node.endswith("A"))

    node_length_map = {}
    for node in start_nodes:
        node_length_map[node] = find_cycle_length(graph, node, instructions)
    print(node_length_map)

    # find the least common multiple of all the cycle lengths
    lcm = math.lcm(*node_length_map.values())
    print(lcm)


def find_cycle_length(graph, start_node, instructions):
    """Find the length of the cycle from start node to end node."""
    current_node = start_node
    step_count = 0

    while not current_node.endswith("Z"):
        curr_instruction = instructions[step_count % len(instructions)]
        current_node = graph[current_node][curr_instruction]
        step_count += 1
    return step_count


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
