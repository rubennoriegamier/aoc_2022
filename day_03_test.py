from typing import Final
from unittest import TestCase, main

from day_03 import part_1, part_2, priority


class TestDay03(TestCase):
    _RUCKSACKS: Final[list[str]] = ['vJrwpWtwJgWrhcsFMMfFFhFp',
                                    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
                                    'PmmdzqPrVvPwwTWBwg',
                                    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
                                    'ttgJtRGJQctTZtZT',
                                    'CrZsJsPPZsGzwwsLwLmpwMDw']

    def test_priority(self):
        for item_type, priority_ in (('a', 1), ('z', 26), ('A', 27), ('Z', 52)):
            with self.subTest(item_type=item_type):
                self.assertEqual(priority(item_type), priority_)

    def test_part_1(self):
        self.assertEqual(part_1(self._RUCKSACKS), 157)

    def test_part_2(self):
        self.assertEqual(part_2(self._RUCKSACKS), 70)


if __name__ == '__main__':
    main()
