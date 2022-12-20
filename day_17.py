from collections import defaultdict
from collections import deque
from itertools import cycle


def main():
    jets: str = input()

    print(part_1_and_2(jets, 2_022))
    print(part_1_and_2(jets, 1_000_000_000_000))


def print_chamber(chamber: deque[list[str]]):
    print(*map(''.join, chamber), sep='\n')


def part_1_and_2(jets: str, rocks: int) -> int:
    chamber = deque()
    jets_len = len(jets)
    jets = cycle(enumerate(jets))
    jet_idx = 0
    rock_idx = 0
    height = 0
    patterns = defaultdict(list)

    chamber.append(list('+-------+'))
    while rock_idx < rocks:
        up = next(y for y in range(len(chamber)) if any(chamber[y][x] != '.' for x in range(1, 8)))

        for _ in range(up - 3):
            del chamber[0]
        for _ in range(3 - up):
            chamber.appendleft(list('|.......|'))

        jet_patterns = patterns[jet_idx % jets_len]
        jet_patterns.append((rock_idx, len(chamber) - 4))
        if (len(jet_patterns) >= 3
                and jet_patterns[-1][0] - jet_patterns[-2][0] == jet_patterns[-2][0] - jet_patterns[-3][0]
                and jet_patterns[-1][1] - jet_patterns[-2][1] == jet_patterns[-2][1] - jet_patterns[-3][1]):
            jumps = (rocks - rock_idx) // (jet_patterns[-1][0] - jet_patterns[-2][0])
            rock_idx += (jet_patterns[-1][0] - jet_patterns[-2][0]) * jumps
            height = (len(chamber) - 4 - jet_patterns[-2][1]) * jumps

            if rock_idx == rocks:
                break

        y = 0
        x = 3

        match rock_idx % 5:
            case 0:
                chamber.appendleft(list('|..####.|'))
                while True:
                    jet_idx, jet = next(jets)

                    if jet == '>':
                        if chamber[y][x + 4] == '.':
                            x += 1
                            chamber[y][x - 1:x + 4] = '.####'
                    elif chamber[y][x - 1] == '.':
                        x -= 1
                        chamber[y][x:x + 5] = '####.'

                    if all(chamber[y + 1][x_] == '.' for x_ in range(x, x + 4)):
                        y += 1
                        chamber[y - 1][x:x + 4] = '....'
                        chamber[y][x:x + 4] = '####'
                    else:
                        break
            case 1:
                chamber.appendleft(list('|...#...|'))
                chamber.appendleft(list('|..###..|'))
                chamber.appendleft(list('|...#...|'))
                while True:
                    jet_idx, jet = next(jets)

                    if jet == '>':
                        if chamber[y][x + 2] == '.' and chamber[y + 1][x + 3] == '.' and chamber[y + 2][x + 2] == '.':
                            x += 1
                            chamber[y][x:x + 2] = '.#'
                            chamber[y + 1][x - 1:x + 3] = '.###'
                            chamber[y + 2][x:x + 2] = '.#'
                    elif chamber[y][x] == '.' and chamber[y + 1][x - 1] == '.' and chamber[y + 2][x] == '.':
                        x -= 1
                        chamber[y][x + 1:x + 3] = '#.'
                        chamber[y + 1][x:x + 4] = '###.'
                        chamber[y + 2][x + 1:x + 3] = '#.'

                    if chamber[y + 2][x] == '.' and chamber[y + 3][x + 1] == '.' and chamber[y + 2][x + 2] == '.':
                        y += 1
                        chamber[y - 1][x + 1] = '.'
                        chamber[y][x:x + 3] = '.#.'
                        chamber[y + 1][x:x + 3] = '###'
                        chamber[y + 2][x + 1] = '#'
                    else:
                        break
            case 2:
                chamber.appendleft(list('|..###..|'))
                chamber.appendleft(list('|....#..|'))
                chamber.appendleft(list('|....#..|'))
                while True:
                    jet_idx, jet = next(jets)

                    if jet == '>':
                        if chamber[y][x + 3] == '.' and chamber[y + 1][x + 3] == '.' and chamber[y + 2][x + 3] == '.':
                            x += 1
                            chamber[y][x + 1:x + 3] = '.#'
                            chamber[y + 1][x + 1:x + 3] = '.#'
                            chamber[y + 2][x - 1:x + 3] = '.###'
                    elif chamber[y][x + 1] == '.' and chamber[y + 1][x + 1] == '.' and chamber[y + 2][x - 1] == '.':
                        x -= 1
                        chamber[y][x + 2:x + 4] = '#.'
                        chamber[y + 1][x + 2:x + 4] = '#.'
                        chamber[y + 2][x:x + 4] = '###.'

                    if chamber[y + 3][x] == '.' and chamber[y + 3][x + 1] == '.' and chamber[y + 3][x + 2] == '.':
                        y += 1
                        chamber[y - 1][x + 2] = '.'
                        chamber[y + 1][x:x + 2] = '..'
                        chamber[y + 2][x:x + 3] = '###'
                    else:
                        break
            case 3:
                chamber.appendleft(list('|..#....|'))
                chamber.appendleft(list('|..#....|'))
                chamber.appendleft(list('|..#....|'))
                chamber.appendleft(list('|..#....|'))
                while True:
                    jet_idx, jet = next(jets)

                    if jet == '>':
                        if all(chamber[y_][x + 1] == '.' for y_ in range(y, y + 4)):
                            x += 1
                            for y_ in range(y, y + 4):
                                chamber[y_][x - 1:x + 1] = '.#'
                    elif all(chamber[y_][x - 1] == '.' for y_ in range(y, y + 4)):
                        x -= 1
                        for y_ in range(y, y + 4):
                            chamber[y_][x:x + 2] = '#.'

                    if chamber[y + 4][x] == '.':
                        y += 1
                        chamber[y - 1][x] = '.'
                        chamber[y + 3][x] = '#'
                    else:
                        break
            case 4:
                chamber.appendleft(list('|..##...|'))
                chamber.appendleft(list('|..##...|'))
                while True:
                    jet_idx, jet = next(jets)

                    if jet == '>':
                        if chamber[y][x + 2] == '.' and chamber[y + 1][x + 2] == '.':
                            x += 1
                            chamber[y][x - 1:x + 2] = '.##'
                            chamber[y + 1][x - 1:x + 2] = '.##'
                    elif chamber[y][x - 1] == '.' and chamber[y + 1][x - 1] == '.':
                        x -= 1
                        chamber[y][x:x + 3] = '##.'
                        chamber[y + 1][x:x + 3] = '##.'

                    if chamber[y + 2][x] == '.' and chamber[y + 2][x + 1] == '.':
                        y += 1
                        chamber[y - 1][x:x + 2] = '..'
                        chamber[y + 1][x:x + 2] = '##'
                    else:
                        break

        rock_idx += 1

    return (height + len(chamber) -
            next(y for y in range(len(chamber)) if any(chamber[y][x] != '.' for x in range(1, 8))) - 1)


if __name__ == '__main__':
    main()
