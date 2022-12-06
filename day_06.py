def main():
    data: str = input()

    print(part_1_and_2(data, 4))
    print(part_1_and_2(data, 14))


def part_1_and_2(data: str, size: int) -> int:
    return next(i for i in range(size, len(data)) if len(set(data[i - size:i])) == size)


if __name__ == '__main__':
    main()
