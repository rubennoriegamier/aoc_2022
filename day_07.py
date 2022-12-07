import fileinput
from collections import Counter
from itertools import islice


def main():
    inputs_and_outputs: list[list[str]] = list(map(str.split, map(str.rstrip, fileinput.input())))

    print(*part_1_and_2(inputs_and_outputs), sep='\n')


def part_1_and_2(inputs_and_outputs: list[list[str]]) -> tuple[int, int]:
    path = []
    sizes = Counter()

    for input_output in islice(inputs_and_outputs, 1, None):
        if input_output[0] == '$':
            if input_output[1] == 'cd':
                if input_output[2] == '..':
                    path.pop()
                else:
                    path.append(input_output[2])
        elif input_output[0] != 'dir':
            size = int(input_output[0])

            sizes['/'] += size
            for i in range(len(path)):
                sizes['/'.join(path[:i + 1])] += size

    return (sum(size for size in sizes.values() if size < 100_000),
            next(size for size in sorted(sizes.values()) if size >= sizes['/'] - 40_000_000))


if __name__ == '__main__':
    main()
