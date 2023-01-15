import fileinput
from itertools import count

import numpy as np
# noinspection PyProtectedMember
from numpy.lib.stride_tricks import as_strided
from scipy.signal import convolve2d


def main():
    grove: list[str] = list(map(str.rstrip, fileinput.input()))

    print(*part_1_and_2(grove, 10), sep='\n')


def part_1_and_2(grove: list[str], rounds: int | None = None) -> tuple[int, int]:
    around = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]], np.uint8)
    grove_ = np.empty((len(grove), len(grove[0])), np.bool_)
    for y, row in enumerate(grove):
        for x, tile in enumerate(row):
            grove_[y, x] = tile == '#'
    part_1 = None

    for round_ in count(1):
        pad_north = grove_[0].any()
        pad_south = grove_[-1].any()
        pad_west = grove_[:, 0].any()
        pad_east = grove_[:, -1].any()

        if pad_north or pad_south or pad_west or pad_east:
            grove_ = np.pad(grove_, ((int(pad_north), int(pad_south)), (int(pad_west), int(pad_east))))

        valid = convolve2d(grove_, around, 'valid') > 0
        valid &= grove_[1:-1, 1:-1]

        ns = as_strided(grove_, (grove_.shape[0], grove_.shape[1] - 2, 3),
                        (grove_.strides[0], 1, 1)).any(2)
        ns ^= True
        we = as_strided(grove_, (grove_.shape[0] - 2, grove_.shape[1], 3),
                        (grove_.strides[0], 1, grove_.strides[0])).any(2)
        we ^= True

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

        grove_[1:-1, 1:-1][n] = False
        grove_[:-2, 1:-1][n] = True
        grove_[1:-1, 1:-1][s] = False
        grove_[2:, 1:-1][s] = True
        grove_[1:-1, 1:-1][w] = False
        grove_[1:-1, :-2][w] = True
        grove_[1:-1, 1:-1][e] = False
        grove_[1:-1, 2:][e] = True

        if round_ == rounds:
            height, width = grove_.shape
            for y in range(height):
                if grove_[y].any():
                    break
                height -= 1
            for y in range(-1, -height - 1, -1):
                if grove_[y].any():
                    break
                height -= 1
            for x in range(width):
                if grove_[:, x].any():
                    break
                width -= 1
            for x in range(-1, -width - 1, -1):
                if grove_[:, x].any():
                    break
                width -= 1
            part_1 = height * width - grove_.sum()


if __name__ == '__main__':
    main()
