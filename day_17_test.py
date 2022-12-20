from unittest import TestCase, main

from day_17 import part_1_and_2


class TestDay17(TestCase):
    _jets: str

    def setUp(self):
        self._jets = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

    def test_part_1(self):
        self.assertEqual(part_1_and_2(self._jets, 2_022), 3_068)

    def test_part_2(self):
        self.assertEqual(part_1_and_2(self._jets, 1_000_000_000_000), 1_514_285_714_288)


if __name__ == '__main__':
    main()
