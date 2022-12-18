from unittest import TestCase, main

from day_16 import parse_valves, part_1_and_2, simplify


class TestDay16(TestCase):
    _part_1: int
    _part_2: int

    def setUp(self):
        rates, valves = parse_valves('''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II''')
        valves = simplify(rates, valves)
        self._part_1, self._part_2 = part_1_and_2(rates, valves)

    def test_part_1(self):
        self.assertEqual(self._part_1, 1_651)

    def test_part_2(self):
        self.assertEqual(self._part_2, 1_707)


if __name__ == '__main__':
    main()
