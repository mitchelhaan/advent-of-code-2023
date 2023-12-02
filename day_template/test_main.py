import pytest
from pathlib import Path

from .main import parse_input_part1, parse_input_part2, part1, part2

sample_input = """
a
b
c
d
"""

sample_data1 = parse_input_part1(sample_input)
sample_data2 = parse_input_part2(sample_input)


def test_parse_input_part1():
    assert len(sample_data1) == 4


def test_parse_input_part2():
    assert len(sample_data2) == 4


def test_part1():
    assert part1(sample_data1) == 4


def test_part2():
    assert part2(sample_data2) == 4


def test_real_data():
    input_file = Path(__file__).parent / "input.txt"

    if not input_file.exists():
        pytest.skip(f"{input_file} not found")
        return

    with open(input_file) as f:
        raw_data = f.read()
        real_data1 = parse_input_part1(raw_data)
        real_data2 = parse_input_part2(raw_data)

    assert part1(real_data1) == 7
    assert part2(real_data2) == 7
