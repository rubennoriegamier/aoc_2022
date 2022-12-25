import fileinput
import re
from collections import deque


def main():
    board_and_path: list[str] = list(map(str.rstrip, fileinput.input()))
    board: list[str] = board_and_path[:-2]
    path: str = board_and_path[-1]

    print(part_1(board, path))
    print(part_2(board, path))


def part_1(board: list[str], path: str) -> int:
    x_min: list[int | None] = [None] * len(board)
    x_max: list[int | None] = [None] * len(board)
    y_min: list[int | None] = [None] * max(map(len, board))
    y_max: list[int | None] = [None] * len(y_min)

    for y, row in enumerate(board):
        for x, tile in enumerate(row):
            if tile != ' ':
                if x_min[y] is None:
                    x_min[y] = x
                x_max[y] = x
                if y_min[x] is None:
                    y_min[x] = y
                y_max[x] = y

    facing = deque([(0, -1), (1, 0), (0, 1), (-1, 0)])
    x = board[0].index('.')
    y = 0

    for turn, *steps in re.findall(r'[RL]\d+', 'R' + path):
        steps = int(''.join(steps))

        facing.rotate(-1 if turn == 'R' else 1)

        for _ in range(steps):
            next_x = x + facing[0][0]
            next_y = y + facing[0][1]

            if next_x < x_min[y]:
                next_x = x_max[y]
            elif next_x > x_max[y]:
                next_x = x_min[y]
            elif next_y < y_min[x]:
                next_y = y_max[x]
            elif next_y > y_max[x]:
                next_y = y_min[x]

            if board[next_y][next_x] == '#':
                break

            x = next_x
            y = next_y

    return (y + 1) * 1_000 + (x + 1) * 4 + facing.index((1, 0))


# Only works with the layout ##
#                            #
#                           ##
#                           #
def part_2(board: list[str], path: str) -> int:
    x_min: list[int | None] = [None] * len(board)
    x_max: list[int | None] = [None] * len(board)
    y_min: list[int | None] = [None] * max(map(len, board))
    y_max: list[int | None] = [None] * len(y_min)
    size = len(board) // 4

    for y, row in enumerate(board):
        for x, tile in enumerate(row):
            if tile != ' ':
                if x_min[y] is None:
                    x_min[y] = x
                x_max[y] = x
                if y_min[x] is None:
                    y_min[x] = y
                y_max[x] = y

    facing = deque([(0, -1), (1, 0), (0, 1), (-1, 0)])
    x = board[0].index('.')
    y = 0

    for turn, *steps in re.findall(r'[RL]\d+', 'R' + path):
        steps = int(''.join(steps))

        facing.rotate(-1 if turn == 'R' else 1)

        for _ in range(steps):
            next_x = x + facing[0][0]
            next_y = y + facing[0][1]
            rotate = 0

            if next_x < x_min[y]:
                match y // size:
                    case 0:
                        next_x = 0
                        next_y = size * 3 - y - 1
                        rotate = 2
                    case 1:
                        next_x = y - size
                        next_y = size * 2
                        rotate = 1
                    case 2:
                        next_x = size
                        next_y = size - (y - size * 2) - 1
                        rotate = 2
                    case 3:
                        next_x = y - size * 2
                        next_y = 0
                        rotate = 1
            elif next_x > x_max[y]:
                match y // size:
                    case 0:
                        next_x = size * 2 - 1
                        next_y = size * 2 + size - y - 1
                        rotate = 2
                    case 1:
                        next_x = size + y
                        next_y = size - 1
                        rotate = 1
                    case 2:
                        next_x = size * 3 - 1
                        next_y = size - (y - size * 2) - 1
                        rotate = 2
                    case 3:
                        next_x = y - size * 2
                        next_y = size * 3 - 1
                        rotate = 1
            elif next_y < y_min[x]:
                match x // size:
                    case 0:
                        next_x = size
                        next_y = size + x
                        rotate = -1
                    case 1:
                        next_x = 0
                        next_y = size * 2 + x
                        rotate = -1
                    case 2:
                        next_x = x - size * 2
                        next_y = size * 4 - 1
                        rotate = 0
            elif next_y > y_max[x]:
                match x // size:
                    case 0:
                        next_x = x + size * 2
                        next_y = 0
                        rotate = 0
                    case 1:
                        next_x = size - 1
                        next_y = x + size * 2
                        rotate = -1
                    case 2:
                        next_x = size * 2 - 1
                        next_y = x - size
                        rotate = -1

            if board[next_y][next_x] == '#':
                break

            x = next_x
            y = next_y
            facing.rotate(rotate)

    return (y + 1) * 1_000 + (x + 1) * 4 + facing.index((1, 0))


if __name__ == '__main__':
    main()
