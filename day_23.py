import fileinput
from collections import deque
from itertools import count
from operator import itemgetter


def main():
    grove: list[str] = list(map(str.rstrip, fileinput.input()))

    print(*part_1_and_2(grove, 10), sep='\n')


def print_elfs(elfs: set[tuple[int, int]]):
    y_min = min(map(itemgetter(0), elfs))
    y_max = max(map(itemgetter(0), elfs))
    x_min = min(map(itemgetter(1), elfs))
    x_max = max(map(itemgetter(1), elfs))

    grid = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]

    for elf_y, elf_x in elfs:
        grid[elf_y - y_min][elf_x - x_min] = '#'

    print(*map(''.join, grid), sep='\n')


def part_1_and_2(grove: list[str], rounds: int | None = None) -> tuple[int, int]:
    elfs = {(y, x)
            for y, row in enumerate(grove)
            for x, tile in enumerate(row)
            if tile == '#'}
    checks = deque(['N', 'S', 'W', 'E'])
    part_1 = None

    for round_ in count(1):
        elfs_ = set()
        moves = {}

        for elf in elfs:
            elf_y, elf_x = elf
            nw = elf_y - 1, elf_x - 1
            nw_check = nw in elfs
            n = elf_y - 1, elf_x
            n_check = n in elfs
            ne = elf_y - 1, elf_x + 1
            ne_check = ne in elfs
            sw = elf_y + 1, elf_x - 1
            sw_check = sw in elfs
            s = elf_y + 1, elf_x
            s_check = s in elfs
            se = elf_y + 1, elf_x + 1
            se_check = se in elfs
            w = elf_y, elf_x - 1
            w_check = w in elfs
            e = elf_y, elf_x + 1
            e_check = e in elfs

            if nw_check or n_check or ne_check or sw_check or s_check or se_check or w_check or e_check:
                for check in checks:
                    match check:
                        case 'N':
                            if not nw_check and not n_check and not ne_check:
                                if (other := moves.pop(n, None)) is None:
                                    moves[n] = elf
                                else:
                                    elfs_.add(elf)
                                    elfs_.add(other)
                                break
                        case 'S':
                            if not sw_check and not s_check and not se_check:
                                if (other := moves.pop(s, None)) is None:
                                    moves[s] = elf
                                else:
                                    elfs_.add(elf)
                                    elfs_.add(other)
                                break
                        case 'W':
                            if not nw_check and not w_check and not sw_check:
                                if (other := moves.pop(w, None)) is None:
                                    moves[w] = elf
                                else:
                                    elfs_.add(elf)
                                    elfs_.add(other)
                                break
                        case 'E':
                            if not ne_check and not e_check and not se_check:
                                if (other := moves.pop(e, None)) is None:
                                    moves[e] = elf
                                else:
                                    elfs_.add(elf)
                                    elfs_.add(other)
                                break
                else:
                    elfs_.add(elf)
            else:
                elfs_.add(elf)

        if not moves:
            return part_1, round_

        elfs = elfs_
        elfs.update(moves)
        checks.rotate(-1)

        if round_ == rounds:
            part_1 = (max(map(itemgetter(0), elfs)) - min(map(itemgetter(0), elfs)) + 1) * \
                     (max(map(itemgetter(1), elfs)) - min(map(itemgetter(1), elfs)) + 1) - len(elfs)


if __name__ == '__main__':
    main()
