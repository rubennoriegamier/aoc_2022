from enum import Enum
from sys import stdin


class Part(Enum):
    ONE = 1
    TWO = 2


def main():
    raw_stacks, raw_steps = stdin.read().split('\n\n')
    stacks = parse_stacks(raw_stacks)
    steps = parse_steps(raw_steps)

    print(part_(Part.ONE, stacks, steps))
    print(part_(Part.TWO, stacks, steps))


def parse_stacks(raw_stacks: str) -> list[list[str]]:
    lines = raw_stacks.splitlines()
    stacks = [[] for _ in range(int(lines[-1].rsplit(maxsplit=1)[-1]))]

    for line in lines[:-1]:
        for i, crate in enumerate(line[1::4]):
            if crate != ' ':
                stacks[i].insert(0, crate)

    return stacks


def parse_steps(raw_steps: str) -> list[tuple[int, int, int]]:
    # noinspection PyTypeChecker
    return [tuple(map(int, raw_step.split()[1::2])) for raw_step in raw_steps.splitlines()]


def part_(part: Part, stacks: list[list[str]], steps: list[tuple[int, int, int]]) -> str:
    stacks = list(map(list.copy, stacks))

    for moves, from_, to in steps:
        stacks[to - 1].extend(stacks[from_ - 1][:-moves - 1:-1] if part == Part.ONE else stacks[from_ - 1][-moves:])
        del stacks[from_ - 1][-moves:]

    return ''.join(stack[-1] for stack in stacks)


if __name__ == '__main__':
    main()
