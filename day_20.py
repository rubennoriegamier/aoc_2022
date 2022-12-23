import fileinput
from functools import partial
from itertools import cycle, islice
from operator import mul


def main():
    numbers: list[int] = list(map(int, fileinput.input()))

    print(decrypt(numbers))
    print(decrypt(numbers, 811_589_153, 10))


def decrypt(numbers: list[int], key: int = 1, times: int = 1) -> int:
    numbers = list(enumerate(map(partial(mul, key), numbers)))

    for number in islice(cycle(numbers.copy()), len(numbers) * times):
        old_idx = numbers.index(number)
        new_idx = (old_idx + number[1]) % (len(numbers) - 1)

        del numbers[old_idx]
        numbers.insert(new_idx, number)

    zero_idx = next(idx for idx, number in enumerate(numbers) if number[1] == 0)

    return (numbers[(zero_idx + 1_000) % len(numbers)][1] +
            numbers[(zero_idx + 2_000) % len(numbers)][1] +
            numbers[(zero_idx + 3_000) % len(numbers)][1])


if __name__ == '__main__':
    main()
