import fileinput


def main():
    pairs: list[tuple[range, range]] = list(map(parse_pair, fileinput.input()))

    print(part_1(pairs))
    print(part_2(pairs))


def parse_range(raw_range: str) -> range:
    return range(*map(int, raw_range.split('-')))


def parse_pair(raw_pair: str) -> tuple[range, range]:
    # noinspection PyTypeChecker
    return tuple(map(parse_range, raw_pair.split(',')))


def part_1(pairs: list[tuple[range, range]]) -> int:
    return sum(1 for (range_a, range_b) in pairs
               if range_a.start <= range_b.start and range_a.stop >= range_b.stop
               or range_b.start <= range_a.start and range_b.stop >= range_a.stop)


def part_2(pairs: list[tuple[range, range]]) -> int:
    return sum(1 for (range_a, range_b) in pairs if range_a.start <= range_b.stop and range_a.stop >= range_b.start)


if __name__ == '__main__':
    main()
