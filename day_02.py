import fileinput
from typing import Final

# A = Rock
# B = Paper
# C = Scissors
# X = Rock
# Y = Paper
# Z = Scissors
SCORES_PART_1: Final[dict[str, int]] = {'A X': 1 + 3, 'A Y': 2 + 6, 'A Z': 3 + 0,
                                        'B X': 1 + 0, 'B Y': 2 + 3, 'B Z': 3 + 6,
                                        'C X': 1 + 6, 'C Y': 2 + 0, 'C Z': 3 + 3}
SCORES_PART_2: Final[dict[str, int]] = {'A X': 3 + 0, 'A Y': 1 + 3, 'A Z': 2 + 6,
                                        'B X': 1 + 0, 'B Y': 2 + 3, 'B Z': 3 + 6,
                                        'C X': 2 + 0, 'C Y': 3 + 3, 'C Z': 1 + 6}


def main():
    strategy_guide: list[str] = list(map(str.rstrip, fileinput.input()))

    print(part_1(strategy_guide))
    print(part_2(strategy_guide))


def part_1(strategy_guide: list[str]) -> int:
    return sum(map(SCORES_PART_1.get, strategy_guide))


def part_2(strategy_guide: list[str]) -> int:
    return sum(map(SCORES_PART_2.get, strategy_guide))


if __name__ == '__main__':
    main()
