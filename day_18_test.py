from unittest import TestCase, main

from day_18 import parse_cube, part_1, part_2


class TestDay18(TestCase):
    _cubes: list[tuple[int, int, int]]

    def setUp(self):
        self._cubes = list(map(parse_cube, ['2,2,2',
                                            '1,2,2',
                                            '3,2,2',
                                            '2,1,2',
                                            '2,3,2',
                                            '2,2,1',
                                            '2,2,3',
                                            '2,2,4',
                                            '2,2,6',
                                            '1,2,5',
                                            '3,2,5',
                                            '2,1,5',
                                            '2,3,5']))

    def test_part_1(self):
        self.assertEqual(part_1(self._cubes), 64)

    def test_part_2(self):
        self.assertEqual(part_2(self._cubes), 58)


if __name__ == '__main__':
    main()
