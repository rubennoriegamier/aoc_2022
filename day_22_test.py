from unittest import TestCase, main

from day_22 import part_1, part_2


class TestDay22(TestCase):
    _board: list[str]
    _path = str

    @classmethod
    def setUpClass(cls):
        cls._board = list(map(str.rstrip, '''        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.'''.splitlines()))
        cls._path = '10R5L5R10L4R5L5'

    def test_part_1(self):
        self.assertEqual(part_1(self._board, self._path), 6_032)

    def test_part_2(self):
        # TODO This does not work with the sample layout
        self.assertEqual(part_2(self._board, self._path), 5_031)


if __name__ == '__main__':
    main()
