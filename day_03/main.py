import re
from typing import List

# https://adventofcode.com/2023/day/3


def has_adjacent_symbol(data, row, col_start, col_end) -> bool:
    symbol_re = re.compile(r"[-+@/$&%=#*]")

    if row > 0 and symbol_re.search(data[row - 1], col_start - 1, col_end + 1):
        return True

    if symbol_re.search(data[row], col_start - 1, col_end + 1):
        return True

    if row + 1 < len(data) and symbol_re.search(data[row + 1], col_start - 1, col_end + 1):
        return True

    return False


def adjacent_numbers(data, row, col) -> List[int]:
    number_re = re.compile(r"\d+")
    numbers = []

    if row > 0:
        for match in number_re.finditer(data[row - 1]):
            if match.start() - 1 <= col <= match.end():
                numbers.append(int(match.group()))

    for match in number_re.finditer(data[row]):
        if match.start() - 1 <= col <= match.end():
            numbers.append(int(match.group()))

    if row + 1 < len(data):
        for match in number_re.finditer(data[row + 1]):
            if match.start() - 1 <= col <= match.end():
                numbers.append(int(match.group()))

    return numbers


def parse_input_part1(data: str) -> List[str]:
    return data.strip().splitlines()


def part1(data: List[str]) -> int:
    total = 0

    for i in range(len(data)):
        for match in re.finditer(r"\d+", data[i]):
            if has_adjacent_symbol(data, i, match.start(), match.end()):
                total += int(match.group())

    return total


def parse_input_part2(data: str) -> List[str]:
    return data.strip().splitlines()


def part2(data: List[str]) -> int:
    total = 0

    for i in range(len(data)):
        for match in re.finditer(r"\*", data[i]):
            numbers = adjacent_numbers(data, i, match.start())
            if len(numbers) == 2:
                total += numbers[0] * numbers[1]

    return total
