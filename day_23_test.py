from unittest import TestCase, main

from day_23 import part_1_and_2


class TestDay23(TestCase):
    _part_1: int
    _part_2: int

    @classmethod
    def setUpClass(cls):
        cls._part_1, cls._part_2 = part_1_and_2(['....#..',
                                                 '..###.#',
                                                 '#...#.#',
                                                 '.#...##',
                                                 '#.###..',
                                                 '##.#.##',
                                                 '.#..#..'], 10)

    def test_part_1(self):
        self.assertEqual(self._part_1, 110)

    def test_part_2(self):
        self.assertEqual(self._part_2, 20)


if __name__ == '__main__':
    main()
