import re
from typing import List, Tuple, Mapping

# https://adventofcode.com/2023/day/2


def parse_game(data: str) -> Tuple[int, str]:
    result = re.match(r"Game (\d+): (.+)", data)
    return (int(result.group(1)), result.group(2))


def parse_color_count(data: str) -> Mapping[str, int]:
    colors = {}
    for count, color in re.findall(r"(\d+)\s+(\w+)", data):
        colors[color] = int(count)
    return colors


def game_is_possible(game: str, bag: str) -> bool:
    game_colors = {}

    for turn in game.split(";"):
        turn_colors = parse_color_count(turn)
        for color, count in turn_colors.items():
            current_max = game_colors.get(color, 0)
            if count > current_max:
                game_colors[color] = count

    bag_colors = parse_color_count(bag)

    for color, count in game_colors.items():
        if count > bag_colors.get(color):
            return False

    return True


def min_cubes(game: str) -> Mapping[str, int]:
    game_colors = {}

    for turn in game.split(";"):
        turn_colors = parse_color_count(turn)
        for color, count in turn_colors.items():
            current_max = game_colors.get(color, 0)
            if count > current_max:
                game_colors[color] = count

    return game_colors


def parse_input_part1(data: str) -> List[str]:
    return data.strip().splitlines()


def part1(data: List[str]) -> int:
    bag = "12 red cubes, 13 green cubes, and 14 blue cubes"
    games = dict(parse_game(x) for x in data)

    possible_games = []
    for game_id, game in games.items():
        if game_is_possible(game, bag):
            possible_games.append(game_id)

    return sum(possible_games)


def parse_input_part2(data: str) -> List[str]:
    return data.strip().splitlines()


def part2(data: List[str]) -> int:
    games = dict(parse_game(x) for x in data)

    game_powers = []
    for game in games.values():
        cubes = min_cubes(game)
        game_powers.append(cubes["red"] * cubes["green"] * cubes["blue"])

    return sum(game_powers)
