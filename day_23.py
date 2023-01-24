import fileinput
from functools import partial
from itertools import count
from operator import eq

import numpy as np
# noinspection PyProtectedMember
from numpy.lib.stride_tricks import as_strided
from scipy.signal import convolve2d


def main():
    grove: list[str] = list(map(str.rstrip, fileinput.input()))

    print(*part_1_and_2(grove, 10), sep='\n')


def part_1_and_2(grove: list[str], rounds: int) -> tuple[int, int]:
    around = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]], np.uint8)
    grove = np.array(list(map(list, map(partial(map, partial(eq, '#')), grove))))
    part_1 = None

    for round_ in count(1):
        pad_north = grove[0].any()
        pad_south = grove[-1].any()
        pad_west = grove[:, 0].any()
        pad_east = grove[:, -1].any()

        if pad_north or pad_south or pad_west or pad_east:
            grove = np.pad(grove, ((int(pad_north), int(pad_south)), (int(pad_west), int(pad_east))))

        valid = np.logical_and(convolve2d(grove, around, 'valid'), grove[1:-1, 1:-1])

        igrove = ~grove
        ns = as_strided(igrove, (igrove.shape[0], igrove.shape[1] - 2, 3),
                        (igrove.strides[0], 1, 1)).all(2)
        we = as_strided(igrove, (igrove.shape[0] - 2, igrove.shape[1], 3),
                        (igrove.strides[0], 1, igrove.strides[0])).all(2)

        n = ns[:-2] & valid
        s = ns[2:] & valid
        w = we[:, :-2] & valid
        e = we[:, 2:] & valid

        match round_ % 4:
            case 1:
                s[n] = False
                w[n] = False
                w[s] = False
                e[n] = False
                e[s] = False
                e[w] = False
            case 2:
                w[s] = False
                e[s] = False
                e[w] = False
                n[s] = False
                n[w] = False
                n[e] = False
            case 3:
                e[w] = False
                n[w] = False
                n[e] = False
                s[w] = False
                s[e] = False
                s[n] = False
            case 0:
                n[e] = False
                s[e] = False
                s[n] = False
                w[e] = False
                w[n] = False
                w[s] = False

        n_ = n.copy()
        n[2:][s[:-2]] = False
        s[:-2][n_[2:]] = False
        w_ = w.copy()
        w[:, 2:][e[:, :-2]] = False
        e[:, :-2][w_[:, 2:]] = False

        if not n.any() and not s.any() and not w.any() and not e.any():
            return part_1, round_

        grove[1:-1, 1:-1][n] = False
        grove[:-2, 1:-1][n] = True
        grove[1:-1, 1:-1][s] = False
        grove[2:, 1:-1][s] = True
        grove[1:-1, 1:-1][w] = False
        grove[1:-1, :-2][w] = True
        grove[1:-1, 1:-1][e] = False
        grove[1:-1, 2:][e] = True

        if round_ == rounds:
            height, width = grove.shape
            for y in range(height):
                if grove[y].any():
                    break
                height -= 1
            for y in range(-1, -height - 1, -1):
                if grove[y].any():
                    break
                height -= 1
            for x in range(width):
                if grove[:, x].any():
                    break
                width -= 1
            for x in range(-1, -width - 1, -1):
                if grove[:, x].any():
                    break
                width -= 1
            part_1 = height * width - grove.sum()


if __name__ == '__main__':
    main()
