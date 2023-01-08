import fileinput
from functools import partial
from itertools import cycle, islice
from operator import mul

import numpy as np


def main():
    numbers: list[int] = list(map(int, fileinput.input()))

    print(decrypt(numbers))
    print(decrypt(numbers, 811_589_153, 10))


def decrypt(numbers: list[int], key: int = 1, times: int = 1) -> int:
    offset = max(-min(numbers) * key, 0)
    numbers = np.fromiter((i << 48 | number + offset
                           for i, number in enumerate(map(partial(mul, key), numbers))), np.uint64, len(numbers))
    aux = np.empty_like(numbers, np.bool_)

    for number in islice(cycle(numbers.copy()), len(numbers) * times):
        old_idx = np.flatnonzero(np.equal(numbers, number, out=aux))[0]
        new_idx = (old_idx + (int(number) & 0xfff_fff_fff_fff) - offset) % (len(numbers) - 1)

        if old_idx < new_idx:
            numbers[old_idx:new_idx] = numbers[old_idx + 1:new_idx + 1]
            numbers[new_idx] = number
        elif new_idx < old_idx:
            numbers[new_idx + 1:old_idx + 1] = numbers[new_idx:old_idx]
            numbers[new_idx] = number

    zero_idx = next(idx for idx, number in enumerate(numbers) if int(number) & 0xfff_fff_fff_fff == offset)

    return ((int(numbers[(zero_idx + 1_000) % len(numbers)]) & 0xfff_fff_fff_fff) +
            (int(numbers[(zero_idx + 2_000) % len(numbers)]) & 0xfff_fff_fff_fff) +
            (int(numbers[(zero_idx + 3_000) % len(numbers)]) & 0xfff_fff_fff_fff) - offset * 3)


if __name__ == '__main__':
    main()
