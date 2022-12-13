import json
from itertools import chain
from operator import mul
from sys import stdin
from typing import Any


# noinspection PyProtectedMember
class Packet:
    _data: list[Any]

    @staticmethod
    def _compare(a: list[Any] | int, b: list[Any] | int) -> int:
        if isinstance(a, list):
            if isinstance(b, list):
                return next(filter(None, map(Packet._compare, a, b)), max(min(len(a) - len(b), 1), -1))
            return Packet._compare(a, [b])
        return Packet._compare([a], b) if isinstance(b, list) else max(min(a - b, 1), -1)

    def __init__(self, data):
        self._data = data

    def __lt__(self, other):
        return self._compare(self._data, other._data) == -1

    def __le__(self, other):
        return self._compare(self._data, other._data) <= 0

    def __gt__(self, other):
        return self._compare(self._data, other._data) == 1

    def __ge__(self, other):
        return self._compare(self._data, other._data) >= 0

    def __eq__(self, other):
        return self._compare(self._data, other._data) == 0

    def __ne__(self, other):
        return self._compare(self._data, other._data) != 0


def main():
    pairs: list[tuple[Packet, Packet]] = list(map(parse_pair, stdin.read().split('\n\n')))

    print(part_1(pairs))
    print(part_2(pairs))


def parse_pair(raw_pair: str) -> tuple[Packet, Packet]:
    # noinspection PyTypeChecker
    return tuple(map(Packet, map(json.loads, raw_pair.split())))


def part_1(pairs: list[tuple[Packet, Packet]]) -> int:
    return sum(i for i, (a, b) in enumerate(pairs, 1) if a <= b)


def part_2(pairs: list[tuple[Packet, Packet]]) -> int:
    divider_packets = Packet([[2]]), Packet([[6]])

    return mul(*(i for i, packet in enumerate(sorted(chain(chain.from_iterable(pairs), divider_packets)), 1)
                 if packet in divider_packets))


if __name__ == '__main__':
    main()
