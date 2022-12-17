from unittest import TestCase, main

from day_15 import Point, parse_coords, part_1, part_2


class TestDay15(TestCase):
    _coords: list[tuple[Point, Point]]

    def setUp(self):
        self._coords = list(map(parse_coords, ['Sensor at x=2, y=18: closest beacon is at x=-2, y=15',
                                               'Sensor at x=9, y=16: closest beacon is at x=10, y=16',
                                               'Sensor at x=13, y=2: closest beacon is at x=15, y=3',
                                               'Sensor at x=12, y=14: closest beacon is at x=10, y=16',
                                               'Sensor at x=10, y=20: closest beacon is at x=10, y=16',
                                               'Sensor at x=14, y=17: closest beacon is at x=10, y=16',
                                               'Sensor at x=8, y=7: closest beacon is at x=2, y=10',
                                               'Sensor at x=2, y=0: closest beacon is at x=2, y=10',
                                               'Sensor at x=0, y=11: closest beacon is at x=2, y=10',
                                               'Sensor at x=20, y=14: closest beacon is at x=25, y=17',
                                               'Sensor at x=17, y=20: closest beacon is at x=21, y=22',
                                               'Sensor at x=16, y=7: closest beacon is at x=15, y=3',
                                               'Sensor at x=14, y=3: closest beacon is at x=15, y=3',
                                               'Sensor at x=20, y=1: closest beacon is at x=15, y=3']))

    def test_part_1(self):
        self.assertEqual(part_1(self._coords, 10), 26)

    def test_part_2(self):
        self.assertEqual(part_2(self._coords, 20), 560_000_11)


if __name__ == '__main__':
    main()
