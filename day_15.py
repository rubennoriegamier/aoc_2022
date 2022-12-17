import fileinput
import re
from bisect import insort
from collections.abc import Iterable
from operator import attrgetter
from typing import Optional

NUMBER_RE = re.compile(r'-?\d+')


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def copy(self) -> 'Point':
        return Point(self.x, self.y)


class Diagonal:
    a: Point
    b: Point

    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'({self.a} -> {self.b})'

    @property
    def slope(self):
        return max(min(self.b.y - self.a.y, 1), -1) if self.a.x < self.b.x else max(min(self.a.y - self.b.y, 1), -1)

    def clamp_x(self, min_: int, max_: int) -> Optional['Diagonal']:
        a, b = sorted([self.a.copy(), self.b.copy()], key=attrgetter('x'))

        if b.x >= min_ and a.x <= max_:
            move = max(min_, a.x) - a.x
            a.x += move
            a.y += move * self.slope
            move = b.x - min(max_, b.x)
            b.x -= move
            b.y -= move * self.slope

            return Diagonal(a, b)

    def clamp_y(self, min_: int, max_: int) -> Optional['Diagonal']:
        a, b = sorted([self.a.copy(), self.b.copy()], key=attrgetter('y'))

        if b.y >= min_ and a.y <= max_:
            move = max(min_, a.y) - a.y
            a.y += move
            a.x += move * self.slope
            move = b.y - min(max_, b.y)
            b.y -= move
            b.x -= move * self.slope

            return Diagonal(a, b)

    def clamp_xy(self, min_: int, max_: int) -> Optional['Diagonal']:
        d = self.clamp_x(min_, max_)

        return d and d.clamp_y(min_, max_)


def main():
    coords: list[tuple[Point, Point]] = list(map(parse_coords, fileinput.input()))

    print(part_1(coords, 2_000_000))
    print(part_2(coords, 4_000_000))


def parse_coords(raw_coords: str) -> tuple[Point, Point]:
    sensor_x, sensor_y, beacon_x, beacon_y = map(int, NUMBER_RE.findall(raw_coords))

    return Point(sensor_x, sensor_y), Point(beacon_x, beacon_y)


def group_ranges(ranges: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    ranges = sorted(ranges)
    grouped_ranges = [ranges[0]]

    for range_ in ranges[1:]:
        if range_[0] - 1 <= grouped_ranges[-1][1]:
            grouped_ranges[-1] = grouped_ranges[-1][0], max(range_[1], grouped_ranges[-1][1])
        else:
            grouped_ranges.append(range_)

    return grouped_ranges


def part_1(coords: list[tuple[Point, Point]], y: int) -> int:
    beacon_xs = set()
    x_ranges = []

    for sensor, beacon in coords:
        beacon_distance = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)
        y_distance = abs(sensor.y - y)
        x_offset = beacon_distance - y_distance

        if x_offset >= 0:
            if beacon.y == y:
                beacon_xs.add(beacon.x)
            insort(x_ranges, (sensor.x - x_offset, sensor.x + x_offset))

    return sum(x_to - x_from + 1 - sum(x_from <= x <= x_to for x in beacon_xs)
               for (x_from, x_to) in group_ranges(x_ranges))


def part_2(coords: list[tuple[Point, Point]], limit: int) -> int:
    diagonal_xs = set()

    for sensor, beacon in coords:
        distance = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)

        diagonal_xs.add(sensor.x + distance + 1 - sensor.y)
        diagonal_xs.add(sensor.x - distance - 1 - sensor.y)

    for x in diagonal_xs:
        if -limit <= x <= limit:
            y_ranges = []

            for sensor, beacon in coords:
                distance = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)

                if sensor.x - distance - sensor.y <= x <= sensor.x + distance - sensor.y:
                    # 234...
                    # 123#..
                    # 01###.
                    # .##S##
                    # ..###.
                    # ...#..
                    diagonal_idx = x - (sensor.x - distance - sensor.y)
                    y_from = sensor.y - diagonal_idx // 2
                    y_to = y_from + distance - (diagonal_idx & 1)
                    diagonal = Diagonal(Point(x + y_from, y_from), Point(x + y_to, y_to)).clamp_xy(0, limit)

                    if diagonal:
                        y_ranges.append((diagonal.a.y, diagonal.b.y))

            y_ranges = group_ranges(y_ranges)

            if len(y_ranges) == 2:
                y = y_ranges[0][1] + 1
                x += y

                return x * 4_000_000 + y


if __name__ == '__main__':
    main()
