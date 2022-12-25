from unittest import TestCase, main

from day_23 import part_1, part_2


class TestDay23(TestCase):
    _grove: list[str]

    @classmethod
    def setUpClass(cls):
        cls._grove = ['....#..',
                      '..###.#',
                      '#...#.#',
                      '.#...##',
                      '#.###..',
                      '##.#.##',
                      '.#..#..']

    def test_part_1(self):
        self.assertEqual(part_1(self._grove), 110)

    def test_part_2(self):
        self.assertEqual(part_2(self._grove), 20)


if __name__ == '__main__':
    main()
