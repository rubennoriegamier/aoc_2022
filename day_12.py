import fileinput
from collections.abc import Iterable

import networkx as nx


def main():
    grid, start, end = parse_grid(map(str.rstrip, fileinput.input()))

    print(*part_1_and_2(grid, start, end), sep='\n')


def parse_grid(raw_grid: Iterable[str]) -> tuple[list[list[int]], tuple[int, int], tuple[int, int]]:
    grid = []
    start = -1, -1
    end = -1, -1

    for y, row in enumerate(raw_grid):
        grid.append([])

        for x, letter in enumerate(row):
            match letter:
                case 'S':
                    start = y, x
                    grid[-1].append(0)
                case 'E':
                    end = y, x
                    grid[-1].append(25)
                case _:
                    grid[-1].append(ord(letter) - 97)

    return grid, start, end


def part_1_and_2(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> tuple[int, int]:
    graph = nx.DiGraph()

    for y, row in enumerate(grid):
        for x, height in enumerate(row):
            yx = y, x

            if y > 0 and grid[y - 1][x] - height < 2:
                graph.add_edge((y - 1, x), yx)
            if y < len(grid) - 1 and grid[y + 1][x] - height < 2:
                graph.add_edge((y + 1, x), yx)
            if x > 0 and row[x - 1] - height < 2:
                graph.add_edge((y, x - 1), yx)
            if x < len(row) - 1 and row[x + 1] - height < 2:
                graph.add_edge((y, x + 1), yx)

    part_1 = len(grid) * len(grid[0]) - 1
    part_2 = part_1

    for yx, length in nx.single_source_shortest_path_length(graph, end).items():
        if grid[yx[0]][yx[1]] == 0:
            if yx == start:
                part_1 = min(part_1, length)
            part_2 = min(part_2, length)

    return part_1, part_2


if __name__ == '__main__':
    main()
