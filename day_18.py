import fileinput
from itertools import chain


def main():
    cubes: list[tuple[int, int, int]] = list(map(parse_cube, fileinput.input()))

    print(part_1(cubes))
    print(part_2(cubes))


def parse_cube(raw_cube: str) -> tuple[int, int, int]:
    # noinspection PyTypeChecker
    return tuple(map(int, raw_cube.split(',')))


def part_1(cubes: list[tuple[int, int, int]]) -> int:
    cubes = set(cubes)
    offsets = [(-1, 0, 0), (1, 0, 0),
               (0, -1, 0), (0, 1, 0),
               (0, 0, -1), (0, 0, 1)]

    return len(list(chain.from_iterable(((x + x_offset, y + y_offset, z + z_offset)
                                         for x_offset, y_offset, z_offset in offsets
                                         if (x + x_offset, y + y_offset, z + z_offset) not in cubes)
                                        for x, y, z in cubes)))


def part_2(cubes: list[tuple[int, int, int]]) -> int:
    cubes = set(cubes)
    offsets = [(-1, 0, 0), (1, 0, 0),
               (0, -1, 0), (0, 1, 0),
               (0, 0, -1), (0, 0, 1)]
    x_min, x_max = 0, 0
    y_min, y_max = 0, 0
    z_min, z_max = 0, 0

    for x, y, z in cubes:
        x_min = min(x_min, x - 1)
        x_max = max(x_max, x + 1)
        y_min = min(y_min, y - 1)
        y_max = max(y_max, y + 1)
        z_min = min(z_min, z - 1)
        z_max = max(z_max, z + 1)

    airs = set()
    air_candidates = [(x_min, y_min, z_min)]

    while air_candidates:
        x, y, z = air_candidates.pop()

        if x_min <= x <= x_max and y_min <= y <= y_max and z_min <= z <= z_max:
            air_candidate = x, y, z

            if air_candidate not in airs and air_candidate not in cubes:
                airs.add(air_candidate)
                for x_offset, y_offset, z_offset in offsets:
                    air_candidates.append((x + x_offset, y + y_offset, z + z_offset))

    return len(list(chain.from_iterable(((x + x_offset, y + y_offset, z + z_offset)
                                         for x_offset, y_offset, z_offset in offsets
                                         if (x + x_offset, y + y_offset, z + z_offset) not in cubes
                                         and (x + x_offset, y + y_offset, z + z_offset) in airs)
                                        for x, y, z in cubes)))


if __name__ == '__main__':
    main()
