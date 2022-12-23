from unittest import TestCase, main

from day_19 import parse_blueprint, part_1_and_2


class TestDay19(TestCase):
    _part_1: int
    _part_2: int

    @classmethod
    def setUpClass(cls):
        blueprints = list(map(parse_blueprint, ['Blueprint 1: Each ore robot costs 4 ore. '
                                                'Each clay robot costs 2 ore. '
                                                'Each obsidian robot costs 3 ore and 14 clay. '
                                                'Each geode robot costs 2 ore and 7 obsidian.',
                                                'Blueprint 2: Each ore robot costs 2 ore. '
                                                'Each clay robot costs 3 ore. '
                                                'Each obsidian robot costs 3 ore and 8 clay. '
                                                'Each geode robot costs 3 ore and 12 obsidian.']))
        cls._part_1, cls._part_2 = part_1_and_2(blueprints)

    def test_part_1(self):
        self.assertEqual(self._part_1, 33)

    def test_part_2(self):
        self.assertEqual(self._part_2, 3_472)


if __name__ == '__main__':
    main()
