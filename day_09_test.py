from unittest import TestCase, main

from day_09 import parse_motion, part_1, part_2


class TestDay09(TestCase):
    _example_1: list[tuple[int, int]]
    _example_2: list[tuple[int, int]]

    def setUp(self):
        self._example_1 = list(map(parse_motion, ['R 4',
                                                  'U 4',
                                                  'L 3',
                                                  'D 1',
                                                  'R 4',
                                                  'D 1',
                                                  'L 5',
                                                  'R 2']))
        self._example_2 = list(map(parse_motion, ['R 5',
                                                  'U 8',
                                                  'L 8',
                                                  'D 3',
                                                  'R 17',
                                                  'D 10',
                                                  'L 25',
                                                  'U 20']))

    def test_part_1(self):
        self.assertEqual(part_1(self._example_1), 13)

    def test_part_2(self):
        for i, (example, result) in enumerate([(self._example_1, 1), (self._example_2, 36)]):
            with self.subTest(i=i):
                self.assertEqual(part_2(example, 10), result)


if __name__ == '__main__':
    main()
