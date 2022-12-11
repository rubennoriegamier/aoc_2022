from collections import deque
from collections.abc import Callable
from functools import partial
from math import lcm
from operator import add, mul
from sys import stdin
from typing import NamedTuple


class MonkeyRules(NamedTuple):
    operation: Callable[[int], int]
    divisible: int
    test_true: int
    test_false: int


def main():
    data: list[tuple[list[int], MonkeyRules]] = list(map(parse_monkey, stdin.read().split('\n\n')))

    print(part_1(data))
    print(part_2(data))


def square(n: int) -> int:
    return n ** 2


def parse_monkey(raw_monkey: str) -> tuple[list[int], MonkeyRules]:
    lines = raw_monkey.splitlines()
    worry_levels = list(map(int, lines[1].split(': ')[1].split(', ')))
    operator, raw_operand = lines[2].split('old ')[1].split()
    if raw_operand == 'old':
        operation = square
    elif operator == '+':
        operation = partial(add, int(raw_operand))
    else:
        operation = partial(mul, int(raw_operand))
    divisible = int(lines[3].split()[-1])
    test_true = int(lines[4].split()[-1])
    test_false = int(lines[5].split()[-1])

    return worry_levels, MonkeyRules(operation, divisible, test_true, test_false)


def part_1(data: list[tuple[list[int], MonkeyRules]]) -> int:
    inspections = [0] * len(data)
    data: list[tuple[deque[int], MonkeyRules]] = [(deque(worry_levels), rules) for worry_levels, rules in data]

    for _ in range(20):
        for i, (worry_levels, rules) in enumerate(data):
            inspections[i] += len(worry_levels)
            while worry_levels:
                worry_level = rules.operation(worry_levels.popleft()) // 3
                data[rules.test_true if worry_level % rules.divisible == 0 else rules.test_false][0].append(worry_level)

    return mul(*sorted(inspections)[-2:])


def part_2(data: list[tuple[list[int], MonkeyRules]]) -> int:
    inspections = [0] * len(data)
    data = [(deque(worry_levels), rules) for worry_levels, rules in data]
    divisibles_lcm = lcm(*(rule.divisible for _, rule in data))

    for _ in range(10_000):
        for i, (worry_levels, rules) in enumerate(data):
            inspections[i] += len(worry_levels)
            while worry_levels:
                worry_level = divisibles_lcm + rules.operation(worry_levels.popleft()) % divisibles_lcm
                data[rules.test_true if worry_level % rules.divisible == 0 else rules.test_false][0].append(worry_level)

    return mul(*sorted(inspections)[-2:])


if __name__ == '__main__':
    main()
