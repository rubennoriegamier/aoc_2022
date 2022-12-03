import fileinput
from functools import reduce
from operator import and_


def main():
    rucksacks: list[str] = list(map(str.rstrip, fileinput.input()))

    print(part_1(rucksacks))
    print(part_2(rucksacks))


def priority(item_type: str) -> int:
    return ord(item_type) - (96 if item_type.islower() else 38)


def part_1(rucksacks: list[str]) -> int:
    return sum(priority((set(rucksack[:len(rucksack) // 2]) & set(rucksack[len(rucksack) // 2:])).pop())
               for rucksack in rucksacks)


def part_2(rucksacks: list[str]) -> int:
    return sum(priority(reduce(and_, map(set, rucksacks[i:i + 3])).pop())
               for i in range(0, len(rucksacks), 3))


if __name__ == '__main__':
    main()
