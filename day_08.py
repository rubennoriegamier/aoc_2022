import fileinput
from collections import defaultdict
from collections.abc import Iterable
from functools import partial


def main():
    grid: list[list[int]] = parse_grid(map(str.rstrip, fileinput.input()))

    print(part_1(grid))
    print(part_2(grid))


def parse_grid(raw_lines: Iterable[str]) -> list[list[int]]:
    return list(map(list, map(partial(map, int), raw_lines)))


def part_1(grid: list[list[int]]) -> int:
    def go_down_and_go_left(grid_: list[list[int]]) -> set[tuple[int, int]]:
        trees = set()
        col_tallest = defaultdict(lambda: -1)

        for y, row in enumerate(grid_):
            row_tallest = -1

            for x, tree in enumerate(row):
                if tree > row_tallest or tree > col_tallest[x]:
                    trees.add((y, x))
                col_tallest[x] = max(col_tallest[x], tree)
                row_tallest = max(row_tallest, tree)

        return trees

    return len(go_down_and_go_left(grid) | {(len(grid) - y - 1, len(grid[0]) - x - 1)
                                            for y, x in go_down_and_go_left([row[::-1] for row in grid[::-1]])})


def part_2(grid: list[list[int]]) -> int:
    return max((x - next((i for i in range(x - 1, -1, -1) if row[i] >= tree), 0)) *
               (next((i for i in range(x + 1, len(row)) if row[i] >= tree), len(row) - 1) - x) *
               (y - next((i for i in range(y - 1, -1, -1) if grid[i][x] >= tree), 0)) *
               (next((i for i in range(y + 1, len(grid)) if grid[i][x] >= tree), len(grid) - 1) - y)
               for y, row in enumerate(grid)
               for x, tree in enumerate(row))


if __name__ == '__main__':
    main()
