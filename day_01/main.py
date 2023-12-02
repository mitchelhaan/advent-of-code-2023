import re
from typing import List

# https://adventofcode.com/2023/day/1

digit_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

digit_re = re.compile(r"(\d|one|two|three|four|five|six|seven|eight|nine)")


def first_digit(data: str) -> int:
    for x in data:
        if x.isdigit():
            return int(x)


def first_digit_or_word(data: str) -> int:
    digit = digit_re.search(data).group(1)

    if len(digit) > 1:
        return digit_map[digit]
    else:
        return int(digit)


def last_digit(data: str) -> int:
    for x in reversed(data):
        if x.isdigit():
            return int(x)


def last_digit_or_word(data: str) -> int:
    digit = None

    for x in range(len(data) - 1, -1, -1):
        res = digit_re.search(data, pos=x)
        if res:
            digit = res.group(1)
            break

    try:
        return int(digit)
    except ValueError:
        return digit_map[digit]


def parse_input_part1(data: str) -> List[str]:
    return [10 * first_digit(x) + last_digit(x) for x in data.strip().splitlines()]


def part1(data: List[int]) -> int:
    return sum(data)


def parse_input_part2(data: str) -> List[str]:
    return [
        10 * first_digit_or_word(x) + last_digit_or_word(x)
        for x in data.strip().splitlines()
    ]


def part2(data: List[str]) -> int:
    return sum(data)
