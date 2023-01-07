import fileinput
from itertools import count, islice

import numpy as np


def main():
    blizzards: list[str] = list(map(str.rstrip, fileinput.input()))

    print(*part_1_and_2(blizzards), sep='\n')


def part_1_and_2(blizzards: list[str]) -> tuple[int, int]:
    blizzards_ = np.zeros((len(blizzards) - 2, len(blizzards[0]) - 2), np.ubyte)
    aux_n_1 = np.empty_like(blizzards_)
    aux_n_2 = np.empty_like(blizzards_)
    path = np.zeros((blizzards_.shape[0] + 2, blizzards_.shape[1]), np.bool_)
    aux_b = path.copy()
    objetives = [-1, 0, -1]
    steps = []

    for y, row in enumerate(islice(blizzards, 1, len(blizzards) - 1)):
        for x, tile in enumerate(islice(row, 1, len(row) - 1)):
            match tile:
                case '<':
                    blizzards_[y, x] = 0b0001
                case 'v':
                    blizzards_[y, x] = 0b0010
                case '>':
                    blizzards_[y, x] = 0b0100
                case '^':
                    blizzards_[y, x] = 0b1000

    path[0, 0] = True

    for i in count(1):
        # <
        np.bitwise_and(blizzards_[:, 1:], 0b0001, out=aux_n_1[:, :-1])
        np.bitwise_and(blizzards_[:, 0], 0b0001, out=aux_n_1[:, -1])

        # v
        np.bitwise_and(blizzards_[:-1, 1:-1], 0b0010, out=aux_n_2[1:, 1:-1])
        np.bitwise_and(blizzards_[-1, 1:-1], 0b0010, out=aux_n_2[0, 1:-1])
        aux_n_1[:, 1:-1] |= aux_n_2[:, 1:-1]

        # >
        np.bitwise_and(blizzards_[:, :-1], 0b0100, out=aux_n_2[:, 1:])
        np.bitwise_and(blizzards_[:, -1], 0b0100, out=aux_n_2[:, 0])
        aux_n_1 |= aux_n_2

        # ^
        np.bitwise_and(blizzards_[1:, 1:-1], 0b1000, out=aux_n_2[:-1, 1:-1])
        np.bitwise_and(blizzards_[0, 1:-1], 0b1000, out=aux_n_2[-1, 1:-1])
        aux_n_1[:, 1:-1] |= aux_n_2[:, 1:-1]

        aux_n_1, blizzards_ = blizzards_, aux_n_1

        aux_b[:] = path
        aux_b[:-1, :] |= path[1:, :]
        aux_b[1:, :] |= path[:-1, :]
        aux_b[:, :-1] |= path[:, 1:]
        aux_b[:, 1:] |= path[:, :-1]
        path, aux_b = aux_b, path
        aux_b[0, 0] = True
        aux_b[-1, -1] = True
        np.equal(blizzards_, 0, out=aux_b[1:-1, :])
        path &= aux_b
        if path[objetives[-1], objetives[-1]]:
            steps.append(i)
            path.fill(False)
            path[objetives[-1], objetives.pop()] = True
            if not objetives:
                return steps[0], steps[-1]


if __name__ == '__main__':
    main()
