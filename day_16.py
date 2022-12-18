from functools import cache, partial
from itertools import combinations_with_replacement
from operator import ne
from sys import stdin


def main():
    rates, valves = parse_valves(stdin.read())

    print(part_1(rates, valves))
    print(part_2(rates, valves))


def parse_valves(raw_report: str) -> tuple[dict[str, int], dict[str, list[str]]]:
    rates = {}
    valves = {}

    for line in raw_report.splitlines():
        if (rate := int(line.split(';')[0][23:])) > 0:
            rates[line[6:8]] = rate
        valves[line[6:8]] = sorted(valve[-2:] for valve in line.split(', '))

    return rates, valves


def part_1(rates: dict[str, int], valves: dict[str, list[str]]) -> int:
    @cache
    def move(closed: tuple[str], minutes: int, valve: str) -> int:
        # Move
        pressure = max(map(partial(move, closed, minutes - 1), valves[valve])) if minutes >= 3 else 0

        # Open
        if valve in closed:
            pressure_ = rates[valve] * (minutes - 1)

            if minutes >= 4 and len(closed) >= 2:
                pressure_ += move(tuple(filter(partial(ne, valve), closed)), minutes - 1, valve)

            pressure = max(pressure, pressure_)

        return pressure

    return move(tuple(rates), 30, 'AA')


def part_2(rates: dict[str, int], valves: dict[str, list[str]]) -> int:
    @cache
    def move(closed: tuple[str], minutes: int, valve_a: str, valve_b: str) -> int:
        pressure = 0

        if valve_a == valve_b:
            if minutes >= 3:
                pressure = max(move(closed, minutes - 1, next_valve_a, next_valve_b)
                               for next_valve_a, next_valve_b
                               in combinations_with_replacement(valves[valve_a], 2))

            if valve_a in closed:
                pressure_ = rates[valve_a] * (minutes - 1)

                if minutes >= 3 and len(closed) >= 2:
                    closed = tuple(filter(partial(ne, valve_a), closed))

                    for next_valve in valves[valve_a]:
                        if valve_a < next_valve:
                            pressure = max(pressure, pressure_ + move(closed, minutes - 1, valve_a, next_valve))
                        else:
                            pressure = max(pressure, pressure_ + move(closed, minutes - 1, next_valve, valve_a))
                else:
                    pressure = max(pressure, pressure_)
        else:
            if minutes >= 3:
                for next_valve_a in valves[valve_a]:
                    for next_valve_b in valves[valve_b]:
                        if next_valve_a < next_valve_b:
                            pressure = max(pressure, move(closed, minutes - 1, next_valve_a, next_valve_b))
                        elif next_valve_a != valve_b or next_valve_b != valve_a:
                            pressure = max(pressure, move(closed, minutes - 1, next_valve_b, next_valve_a))

            if valve_a in closed:
                pressure_ = rates[valve_a] * (minutes - 1)

                if valve_b in closed:
                    pressure_ += rates[valve_b] * (minutes - 1)

                    if minutes >= 4 and len(closed) >= 3:
                        pressure_ += move(tuple(valve for valve in closed if valve != valve_a and valve != valve_b),
                                          minutes - 1, valve_a, valve_b)

                    pressure = max(pressure, pressure_)
                elif minutes >= 3 and len(closed) >= 2:
                    closed = tuple(filter(partial(ne, valve_a), closed))

                    for next_valve in valves[valve_b]:
                        if valve_a < next_valve:
                            pressure = max(pressure, pressure_ + move(closed, minutes - 1, valve_a, next_valve))
                        else:
                            pressure = max(pressure, pressure_ + move(closed, minutes - 1, next_valve, valve_a))
                else:
                    pressure = max(pressure, pressure_)
            elif valve_b in closed:
                pressure_ = rates[valve_b] * (minutes - 1)

                if minutes >= 3 and len(closed) >= 2:
                    closed = tuple(filter(partial(ne, valve_b), closed))

                    for next_valve in valves[valve_a]:
                        if valve_b < next_valve:
                            pressure = max(pressure, pressure_ + move(closed, minutes - 1, valve_b, next_valve))
                        else:
                            pressure = max(pressure, pressure_ + move(closed, minutes - 1, next_valve, valve_b))
                else:
                    pressure = max(pressure, pressure_)

        return pressure

    return move(tuple(rates), 26, 'AA', 'AA')


if __name__ == '__main__':
    main()
