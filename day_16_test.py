from unittest import TestCase, main

from day_16 import parse_valves, part_1, part_2


class TestDay16(TestCase):
    _rates: dict[str, int]
    _valves: dict[str, list[str]]

    def setUp(self):
        self._rates, self._valves = parse_valves('''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II''')

    def test_part_1(self):
        self.assertEqual(part_1(self._rates, self._valves), 1_651)

    def test_part_2(self):
        self.assertEqual(part_2(self._rates, self._valves), 1_707)


if __name__ == '__main__':
    main()
