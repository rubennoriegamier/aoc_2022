import fileinput
from collections import Counter, deque
from itertools import count
from operator import itemgetter


def main():
    grove: list[str] = list(map(str.rstrip, fileinput.input()))

    print(part_1(grove))
    print(part_2(grove))


def print_elfs(elfs: set[tuple[int, int]]):
    y_min = min(map(itemgetter(0), elfs))
    y_max = max(map(itemgetter(0), elfs))
    x_min = min(map(itemgetter(1), elfs))
    x_max = max(map(itemgetter(1), elfs))

    grid = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]

    for elf_y, elf_x in elfs:
        grid[elf_y - y_min][elf_x - x_min] = '#'

    print(*map(''.join, grid), sep='\n')


def part_1(grove: list[str]) -> int:
    elfs = {(y, x)
            for y, row in enumerate(grove)
            for x, tile in enumerate(row)
            if tile == '#'}
    checks = deque(['N', 'S', 'W', 'E'])

    for r in range(10):
        elfs_ = set()
        moves = []
        times = Counter()

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
                            if nw not in elfs and n not in elfs and ne not in elfs:
                                moves.append((elf, n))
                                times[n] += 1
                                break
                        case 'S':
                            if sw not in elfs and s not in elfs and se not in elfs:
                                moves.append((elf, s))
                                times[s] += 1
                                break
                        case 'W':
                            if nw not in elfs and w not in elfs and sw not in elfs:
                                moves.append((elf, w))
                                times[w] += 1
                                break
                        case 'E':
                            if ne not in elfs and e not in elfs and se not in elfs:
                                moves.append((elf, e))
                                times[e] += 1
                                break
                else:
                    elfs_.add(elf)
            else:
                elfs_.add(elf)

        elfs = elfs_
        elfs.update(destination if times[destination] == 1 else origin for origin, destination in moves)
        checks.rotate(-1)

    return (max(map(itemgetter(0), elfs)) - min(map(itemgetter(0), elfs)) + 1) * \
           (max(map(itemgetter(1), elfs)) - min(map(itemgetter(1), elfs)) + 1) - len(elfs)


def part_2(grove: list[str]) -> int:
    elfs = {(y, x)
            for y, row in enumerate(grove)
            for x, tile in enumerate(row)
            if tile == '#'}
    checks = deque(['N', 'S', 'W', 'E'])

    for round_ in count(1):
        elfs_ = set()
        moves = []
        times = Counter()

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
                            if nw not in elfs and n not in elfs and ne not in elfs:
                                moves.append((elf, n))
                                times[n] += 1
                                break
                        case 'S':
                            if sw not in elfs and s not in elfs and se not in elfs:
                                moves.append((elf, s))
                                times[s] += 1
                                break
                        case 'W':
                            if nw not in elfs and w not in elfs and sw not in elfs:
                                moves.append((elf, w))
                                times[w] += 1
                                break
                        case 'E':
                            if ne not in elfs and e not in elfs and se not in elfs:
                                moves.append((elf, e))
                                times[e] += 1
                                break
                else:
                    elfs_.add(elf)
            else:
                elfs_.add(elf)

        if not moves:
            return round_
        elfs = elfs_
        elfs.update(destination if times[destination] == 1 else origin for origin, destination in moves)
        checks.rotate(-1)

    return (max(map(itemgetter(0), elfs)) - min(map(itemgetter(0), elfs)) + 1) * \
           (max(map(itemgetter(1), elfs)) - min(map(itemgetter(1), elfs)) + 1) - len(elfs)


if __name__ == '__main__':
    main()
