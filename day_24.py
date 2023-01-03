import fileinput
from itertools import chain, count, islice
from time import time

import numpy as np

OFFSETS = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]


def main():
    blizzards: list[str] = list(map(str.rstrip, fileinput.input()))

    t = time()
    print(*part_1_and_2(blizzards), sep='\n')
    print(round((time() - t) * 1_000, 2))


def part_1_and_2(blizzards: list[str]) -> tuple[int, int]:
    blizzards_ = np.zeros((len(blizzards) - 2, len(blizzards[0]) - 2), np.ubyte)
    aux_n_1 = np.empty_like(blizzards_)
    aux_n_2 = np.empty_like(blizzards_)
    aux_b = np.empty_like(blizzards_, np.bool_)
    height = blizzards_.shape[0]
    width = blizzards_.shape[1]
    prev_nodes = {(-1, 0)}
    objetives = [height, -1, height]
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
        curr_nodes = set()

        for curr_node in chain(zip(*np.where(np.equal(blizzards_, 0, out=aux_b))), [(-1, 0), (height, width - 1)]):
            # noinspection PyTupleAssignmentBalance
            y, x = curr_node

            for y_offset, x_offset in OFFSETS:
                if (y + y_offset, x + x_offset) in prev_nodes:
                    curr_nodes.add(curr_node)
                    break
            else:
                continue

            if y == objetives[-1]:
                steps.append(i)
                curr_nodes = {(height, width - 1) if objetives.pop() == height else (-1, 0)}
                break

        if not objetives:
            break

        prev_nodes = curr_nodes

    return steps[0], steps[-1]


if __name__ == '__main__':
    main()
