from unittest import TestCase, main

from day_04 import parse_pair, part_1, part_2


class TestDay04(TestCase):
    _pairs: list[tuple[range, range]]

    def setUp(self):
        self._pairs = list(map(parse_pair, ['2-4,6-8',
                                            '2-3,4-5',
                                            '5-7,7-9',
                                            '2-8,3-7',
                                            '6-6,4-6',
                                            '2-6,4-8']))

    def test_part_1(self):
        self.assertEqual(part_1(self._pairs), 2)

    def test_part_2(self):
        self.assertEqual(part_2(self._pairs), 4)


if __name__ == '__main__':
    main()
