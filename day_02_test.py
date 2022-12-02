from typing import Final
from unittest import TestCase, main

from day_02 import part_1, part_2


class TestDay02(TestCase):
    _STRATEGY_GUIDE: Final[list[str]] = ['A Y', 'B X', 'C Z']

    def test_part_1(self):
        self.assertEqual(part_1(self._STRATEGY_GUIDE), 15)

    def test_part_2(self):
        self.assertEqual(part_2(self._STRATEGY_GUIDE), 12)


if __name__ == '__main__':
    main()
