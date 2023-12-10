#!/usr/bin/env python3

import fileinput


def main():
    history_lines = [[int(num) for num in line.split()] for line in fileinput.input()]
    prediction_sum = sum(predict(line) for line in history_lines)
    print(prediction_sum)


def predict(history_line):
    """Predict the next number in line."""
    all_lines = [history_line]
    last_line = history_line

    # compute until last line is all zeros
    while True:
        next_line = compute_next_line(last_line)
        if all(num == 0 for num in next_line):
            break
        all_lines.append(next_line)
        last_line = next_line

    predicted_number = 0
    for line in all_lines[::-1]:
        predicted_number = line[0] - predicted_number

    return predicted_number


def compute_next_line(last_line):
    next_line = []
    for i in range(1, len(last_line)):
        next_line.append(last_line[i] - last_line[i - 1])

    return next_line

if __name__ == "__main__":
    main()
