import fileinput
from collections.abc import Iterable
from functools import cache
from itertools import pairwise


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @classmethod
    def parse(cls, raw_point: str) -> 'Point':
        return cls(*map(int, raw_point.split(',')))


class Path:
    points: list[Point]

    def __init__(self, points: Iterable[Point]):
        self.points = list(points)

    @classmethod
    def parse(cls, raw_path: str) -> 'Path':
        return cls(map(Point.parse, raw_path.split(' -> ')))


class Cave:
    sand_x: int
    scan: list[list[str]]

    def __init__(self, paths: list[Path]):
        x_min = None
        x_max = None
        y_max = None

        for path in paths:
            for point in path.points:
                x_min = point.x if x_min is None else min(x_min, point.x)
                x_max = point.x if x_max is None else max(x_max, point.x)
                y_max = point.y if y_max is None else max(y_max, point.y)

        self.sand_x = 500 - x_min
        self.scan = [['.'] * (x_max - x_min + 1) for _ in range(y_max + 1)]

        for path in paths:
            for point_a, point_b in pairwise(path.points):
                if point_a.x == point_b.x:
                    for y in range(min(point_a.y, point_b.y), max(point_a.y, point_b.y) + 1):
                        self.scan[y][point_a.x - x_min] = '#'
                else:
                    for x in range(min(point_a.x, point_b.x), max(point_a.x, point_b.x) + 1):
                        self.scan[point_a.y][x - x_min] = '#'

    def __repr__(self):
        return '\n'.join(map(''.join, self.scan))

    def part_1(self) -> int:
        n = 0

        while True:
            x = self.sand_x
            y = 0
            move = True

            while move:
                move = False

                while y + 1 < len(self.scan) and self.scan[y + 1][x] == '.':
                    y += 1
                    move = True
                if y + 1 < len(self.scan):
                    if x > 0 and self.scan[y + 1][x - 1] == '.':
                        x -= 1
                        y += 1
                        move = True
                    elif x + 1 < len(self.scan[0]) and self.scan[y + 1][x + 1] == '.':
                        x += 1
                        y += 1
                        move = True

            if x == 0 or x + 1 == len(self.scan[0]) or y + 1 == len(self.scan):
                return n

            self.scan[y][x] = 'o'
            n += 1

    def part_2(self) -> int:
        @cache
        def sand(y_: int, x_: int) -> bool:
            return (self.sand_x - y_ <= x_ <= self.sand_x + y_
                    and (y_ == 0 or
                         (x_ < 0 or x_ >= len(self.scan[0]) or y_ == len(self.scan) or self.scan[y_][x_] != '#')
                         and (sand(y_ - 1, x_ - 1) or sand(y_ - 1, x_) or sand(y_ - 1, x_ + 1))))

        return sum(1
                   for y in range(len(self.scan), -1, -1)
                   for x in range(self.sand_x - y, self.sand_x + y + 1)
                   if sand(y, x))


def main():
    paths: list[Path] = list(map(Path.parse, fileinput.input()))
    cave: Cave = Cave(paths)

    print(cave.part_1())
    print(cave.part_2())


if __name__ == '__main__':
    main()
