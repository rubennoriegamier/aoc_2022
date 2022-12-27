import fileinput

DIGITS = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}


def main():
    snafu_numbers: list[str] = list(map(str.rstrip, fileinput.input()))

    print(part_1(snafu_numbers))


def from_snafu(number: str | list[str]) -> int:
    return sum(5 ** (len(number) - i - 1) * DIGITS[number[i]] for i in range(len(number)))


def part_1(snafu_numbers: list[str]) -> str:
    n = sum(map(from_snafu, snafu_numbers))

    min_ = ['1']
    max_ = ['2']

    while not (from_snafu(min_) <= n <= from_snafu(max_)):
        min_.append('=')
        max_.append('2')

    for i in range(len(min_)):
        for digit in '=-012':
            min_[i] = digit
            max_[i] = digit

            if from_snafu(min_) <= n <= from_snafu(max_):
                break

    return ''.join(min_)


if __name__ == '__main__':
    main()
