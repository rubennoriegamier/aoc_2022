from unittest import TestCase, main

from day_12 import parse_grid, part_1_and_2


class TestDay12(TestCase):
    _part_1: int
    _part_2: int

    def setUp(self):
        self._part_1, self._part_2 = part_1_and_2(*parse_grid(['Sabqponm',
                                                               'abcryxxl',
                                                               'accszExk',
                                                               'acctuvwj',
                                                               'abdefghi']))

    def test_part_1(self):
        self.assertEqual(self._part_1, 31)

    def test_part_2(self):
        self.assertEqual(self._part_2, 29)


if __name__ == '__main__':
    main()
