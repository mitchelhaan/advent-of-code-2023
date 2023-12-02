import pytest
from pathlib import Path

from .main import (
    first_digit,
    first_digit_or_word,
    last_digit,
    last_digit_or_word,
    parse_input_part1,
    parse_input_part2,
    part1,
    part2,
)


def test_first_digit():
    assert first_digit("1234") == 1
    assert first_digit("a1234b") == 1
    assert first_digit("five1234six") == 1
    assert first_digit_or_word("one2three4") == 1


def test_last_digit():
    assert last_digit("1234") == 4
    assert last_digit("a1234b") == 4
    assert last_digit("five1234six") == 4
    assert last_digit_or_word("one2three4") == 4
    assert last_digit_or_word("one2three4five") == 5


sample_input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

sample_input2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

sample_data1 = parse_input_part1(sample_input)
sample_data2 = parse_input_part2(sample_input2)


def test_parse_input_part1():
    assert sample_data1 == [12, 38, 15, 77]


def test_parse_input_part2():
    assert sample_data2 == [29, 83, 13, 24, 42, 14, 76]


def test_part1():
    assert part1(sample_data1) == 142


def test_part2():
    assert part2(sample_data2) == 281


def test_real_data():
    input_file = Path(__file__).parent / "input.txt"

    if not input_file.exists():
        pytest.skip(f"{input_file} not found")
        return

    with open(input_file) as f:
        raw_data = f.read()
        real_data1 = parse_input_part1(raw_data)
        real_data2 = parse_input_part2(raw_data)

    assert part1(real_data1) == 55017
    assert part2(real_data2) == 53539
