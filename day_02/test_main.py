import pytest
from pathlib import Path

from .main import (
    parse_game,
    parse_color_count,
    game_is_possible,
    min_cubes,
    parse_input_part1,
    parse_input_part2,
    part1,
    part2,
)


def test_parse_game():
    game = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert parse_game(game) == (1, "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")


def test_parse_color_count():
    bag = "12 red cubes, 13 green cubes, and 14 blue cubes"
    assert parse_color_count(bag) == {"red": 12, "green": 13, "blue": 14}


def test_game_is_possible():
    bag = "12 red cubes, 13 green cubes, and 14 blue cubes"
    assert game_is_possible("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", bag)
    assert game_is_possible(
        "1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", bag
    )
    assert not game_is_possible(
        "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", bag
    )


def test_min_cubes():
    assert min_cubes("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == {
        "red": 4,
        "green": 2,
        "blue": 6,
    }
    assert min_cubes("1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue") == {
        "red": 1,
        "green": 3,
        "blue": 4,
    }


sample_input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

sample_data1 = parse_input_part1(sample_input)
sample_data2 = parse_input_part2(sample_input)


def test_parse_input_part1():
    assert len(sample_data1) == 5


def test_parse_input_part2():
    assert len(sample_data2) == 5


def test_part1():
    assert part1(sample_data1) == 8


def test_part2():
    assert part2(sample_data2) == 2286


def test_real_data():
    input_file = Path(__file__).parent / "input.txt"

    if not input_file.exists():
        pytest.skip(f"{input_file} not found")
        return

    with open(input_file) as f:
        raw_data = f.read()
        real_data1 = parse_input_part1(raw_data)
        real_data2 = parse_input_part2(raw_data)

    assert part1(real_data1) == 2156
    assert part2(real_data2) == 66909
