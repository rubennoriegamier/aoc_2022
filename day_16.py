from functools import cache, partial
from itertools import combinations
from operator import ne
from sys import stdin

import networkx as nx
from more_itertools import set_partitions


def main():
    rates, valves = parse_valves(stdin.read())
    valves = simplify(rates, valves)

    print(*part_1_and_2(rates, valves), sep='\n')


def parse_valves(raw_report: str) -> tuple[dict[str, int], dict[str, list[str]]]:
    rates = {}
    valves = {}

    for line in raw_report.splitlines():
        if (rate := int(line.split(';')[0][23:])) > 0:
            rates[line[6:8]] = rate
        valves[line[6:8]] = sorted(valve[-2:] for valve in line.split(', '))

    return rates, valves


def simplify(rates: dict[str, int], valves: dict[str, list[str]]) -> dict[str, list[tuple[str, int]]]:
    weighted_valves = nx.Graph()

    for valve, neighbours in valves.items():
        for neighbour in neighbours:
            weighted_valves.add_edge(valve, neighbour, weight=1)

    while True:
        valves_to_remove = set()

        for valve in weighted_valves:
            if valve != 'AA' and valve not in rates and not valves_to_remove.intersection(weighted_valves[valve]):
                for valve_a, valve_b in combinations(weighted_valves[valve], 2):
                    weight = weighted_valves[valve][valve_a]['weight'] + weighted_valves[valve][valve_b]['weight']
                    edge = weighted_valves.get_edge_data(valve_a, valve_b)

                    if edge is None or weight < edge['weight']:
                        weighted_valves.add_edge(valve_a, valve_b, weight=weight)
                valves_to_remove.add(valve)

        if valves_to_remove:
            weighted_valves.remove_nodes_from(valves_to_remove)
        else:
            break

    return {valve: [(neighbour, attrs['weight']) for neighbour, attrs in weighted_valves[valve].items()]
            for valve in weighted_valves}


def part_1_and_2(rates: dict[str, int], valves: dict[str, list[tuple[str, int]]]) -> tuple[int, int]:
    @cache
    def move(closed: tuple[str], minutes: int, valve: str) -> int:
        # Move
        pressure = max((move(closed, minutes - distance, neighbour)
                        for neighbour, distance in valves[valve]
                        if minutes >= distance + 2), default=0)

        # Open
        if valve in closed:
            pressure_ = rates[valve] * (minutes - 1)

            if minutes >= 4 and len(closed) >= 2:
                pressure_ += move(tuple(filter(partial(ne, valve), closed)), minutes - 1, valve)

            pressure = max(pressure, pressure_)

        return pressure

    return move(tuple(rates), 30, 'AA'), max(move(tuple(closed_a), 26, 'AA') + move(tuple(closed_b), 26, 'AA')
                                             for closed_a, closed_b in set_partitions(rates, 2))


if __name__ == '__main__':
    main()
