import fileinput
from itertools import accumulate, chain
from textwrap import wrap


def main():
    instructions: list[int] = list(map(parse_instruction, map(str.rstrip, fileinput.input())))

    print(part_1(instructions))
    print(part_2(instructions))


def parse_instruction(raw_instruction: str) -> int:
    return 0 if raw_instruction == 'noop' else int(raw_instruction.split()[1])


def part_1(instructions: list[int]) -> int:
    return sum(cycle * register for cycle, register in
               enumerate(accumulate(chain.from_iterable([0] if instruction == 0 else [0, instruction]
                                                        for instruction in instructions), initial=1), 1)
               if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220)


def part_2(instructions: list[int]) -> str:
    return '\n'.join(wrap(''.join('#' if register - 1 <= cycle % 40 <= register + 1 else ' ' for cycle, register in
                                  enumerate(accumulate(chain.from_iterable([0] if instruction == 0 else [0, instruction]
                                                                           for instruction in instructions),
                                                       initial=1))), 40))[:-2]


if __name__ == '__main__':
    main()
