from bisect import bisect
from operator import add, floordiv, mul, sub
from sys import stdin
from typing import Callable


def main():
    jobs: dict[str, int | tuple[Callable[[int, int], int], str, str]] = parse_jobs(stdin.read())

    print(part_1(jobs))
    print(part_2(jobs))


def parse_jobs(raw_jobs: str) -> dict[str, int | tuple[Callable[[int, int], int], str, str]]:
    jobs = {}

    for raw_job in raw_jobs.splitlines():
        parts = raw_job.split()

        if len(parts) == 2:
            jobs[parts[0][:-1]] = int(parts[1])
        else:
            match parts[2]:
                case '+':
                    jobs[parts[0][:-1]] = add, parts[1], parts[3]
                case '-':
                    jobs[parts[0][:-1]] = sub, parts[1], parts[3]
                case '*':
                    jobs[parts[0][:-1]] = mul, parts[1], parts[3]
                case '/':
                    jobs[parts[0][:-1]] = floordiv, parts[1], parts[3]

    return jobs


def part_1(jobs: dict[str, int | tuple[Callable[[int, int], int], str, str]]) -> int:
    def get_value(name: str) -> int:
        value = jobs[name]

        return value if isinstance(value, int) else value[0](get_value(value[1]), get_value(value[2]))

    return get_value('root')


# noinspection PyArgumentList,PyTypeChecker
def part_2(jobs: dict[str, int | tuple[Callable[[int, int], int], str, str]]) -> int:
    def reduce(name: str) -> int:
        if name != 'humn':
            value = jobs[name]

            if isinstance(value, int):
                return value

            operand_a = reduce(value[1])
            operand_b = reduce(value[2])

            if operand_a is not None and operand_b is not None:
                jobs[name] = value[0](operand_a, operand_b)

                return jobs[name]

    reduce('root')

    def get_value(name: str) -> int | tuple[int, int]:
        value = jobs[name]

        if name == 'root':
            return get_value(value[1]), get_value(value[2])

        return value if isinstance(value, int) else value[0](get_value(value[1]), get_value(value[2]))

    def bisect_key(humn: int):
        jobs['humn'] = humn

        return get_value('root')[0]

    a, b = get_value('root')
    a_ = bisect_key(jobs['humn'] + b)
    c = max(a, b)

    if a < a_:
        jobs['humn'] = bisect(range(c), b, key=bisect_key)

        while abs(sub(*get_value('root'))) > 10:
            c *= 2
            jobs['humn'] = bisect(range(c), b, key=bisect_key)
    else:
        jobs['humn'] = range(c, 0, -1)[bisect(range(c, 0, -1), b - 1, key=bisect_key)]

        while abs(sub(*get_value('root'))) > 10:
            c *= 2
            jobs['humn'] = range(c, 0, -1)[bisect(range(c, 0, -1), b, key=bisect_key)]

    humn = jobs['humn']

    for offset in range(-20, 21):
        if bisect_key(humn + offset) == b:
            return jobs['humn']


if __name__ == '__main__':
    main()
