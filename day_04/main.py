import re
from dataclasses import dataclass
from typing import List

# https://adventofcode.com/2023/day/4


@dataclass
class Card:
    id: int
    winning_numbers: List[int]
    played_numbers: List[int]


def parse_card(data: str) -> Card:
    match = re.match(r"Card\s+(\d+):\s*([\d\s]+)\s*\|\s*([\d\s]+)", data)
    return Card(
        id=int(match.group(1)),
        winning_numbers=list(map(int, match.group(2).split())),
        played_numbers=list(map(int, match.group(3).split())),
    )


def matching_numbers(card: Card) -> set[int]:
    return set(card.played_numbers).intersection(set(card.winning_numbers))


def parse_input_part1(data: str) -> List[Card]:
    return list(parse_card(x) for x in data.strip().splitlines())


def part1(cards: List[Card]) -> int:
    total = 0

    for card in cards:
        matching = len(matching_numbers(card))
        if matching > 0:
            total += 1 << (matching - 1)

    return total


def parse_input_part2(data: str) -> List[Card]:
    return parse_input_part1(data)


def part2(cards: List[Card]) -> int:
    counts = [1] * len(cards)

    for i, card in enumerate(cards):
        matching = len(matching_numbers(card))
        for j in range(i + 1, i + 1 + matching):
            counts[j] += counts[i]

    return sum(counts)
