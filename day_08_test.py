from unittest import TestCase, main

from day_08 import parse_grid, part_1, part_2


class TestDay08(TestCase):
    _grid: list[list[int]]

    def setUp(self):
        self._grid = parse_grid(['30373',
                                 '25512',
                                 '65332',
                                 '33549',
                                 '35390'])

    def test_part_1(self):
        self.assertEqual(part_1(self._grid), 21)

    def test_part_2(self):
        self.assertEqual(part_2(self._grid), 8)


if __name__ == '__main__':
    main()
