from typing import Final
from unittest import TestCase, main

from day_01 import parse_sorted_sums, part_1, part_2


class TestDay01(TestCase):
    _RAW_INPUT: Final[str] = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
    _sorted_sums: list[int]

    def setUp(self):
        self._sorted_sums = parse_sorted_sums(self._RAW_INPUT)

    def test_parse_sorted_sums(self):
        self.assertListEqual(self._sorted_sums, [4_000, 6_000, 10_000, 11_000, 24_000])

    def test_part_1(self):
        self.assertEqual(part_1(self._sorted_sums), 24_000)

    def test_part_2(self):
        self.assertEqual(part_2(self._sorted_sums), 45_000)


if __name__ == '__main__':
    main()
