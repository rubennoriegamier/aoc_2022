from unittest import TestCase, main

from day_14 import Cave, Path


class TestDay14(TestCase):
    _cave: Cave

    def setUp(self):
        self._cave = Cave(list(map(Path.parse, ['498,4 -> 498,6 -> 496,6',
                                                '503,4 -> 502,4 -> 502,9 -> 494,9'])))

    def test_part_1(self):
        self.assertEqual(self._cave.part_1(), 24)

    def test_part_2(self):
        self.assertEqual(self._cave.part_2(), 93)


if __name__ == '__main__':
    main()
