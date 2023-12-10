import pytest
from pathlib import Path

from .main import Card, parse_card, matching_numbers, parse_input_part1, parse_input_part2, part1, part2

sample_input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

card1 = Card(id=1, winning_numbers=[41, 48, 83, 86, 17], played_numbers=[83, 86, 6, 31, 17, 9, 48, 53])

sample_data1 = parse_input_part1(sample_input)
sample_data2 = parse_input_part2(sample_input)


def test_parse_card():
    card1_str = sample_input.strip().splitlines()[0]
    assert parse_card(card1_str) == card1


def test_matching_numbers():
    assert matching_numbers(card1) == set([48, 83, 17, 86])


def test_parse_input_part1():
    assert len(sample_data1) == 6


def test_parse_input_part2():
    assert len(sample_data2) == 6


def test_part1():
    assert part1(sample_data1) == 13


def test_part2():
    assert part2(sample_data2) == 30


def test_real_data():
    input_file = Path(__file__).parent / "input.txt"

    if not input_file.exists():
        pytest.skip(f"{input_file} not found")
        return

    with open(input_file) as f:
        raw_data = f.read()
        real_data1 = parse_input_part1(raw_data)
        real_data2 = parse_input_part2(raw_data)

    assert part1(real_data1) == 22674
    assert part2(real_data2) == 5747443
