from functools import partial
from sys import stdin


def main():
    sorted_sums = parse_sorted_sums(stdin.read())

    print(part_1(sorted_sums))
    print(part_2(sorted_sums))


def parse_sorted_sums(raw_input: str) -> list[int]:
    return sorted(map(sum, map(partial(map, int), map(str.split, raw_input.split('\n\n')))))


def part_1(sorted_sums: list[int]) -> int:
    return sorted_sums[-1]


def part_2(sorted_sums: list[int]) -> int:
    return sum(sorted_sums[-3:])


if __name__ == '__main__':
    main()
