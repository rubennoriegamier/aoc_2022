from unittest import TestCase, main

from day_13 import Packet, parse_pair, part_1, part_2


class TestDay13(TestCase):
    _pairs: list[tuple[Packet, Packet]]

    def setUp(self):
        self._pairs = list(map(parse_pair, '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''.split('\n\n')))

    def test_part_1(self):
        self.assertEqual(part_1(self._pairs), 13)

    def test_part_2(self):
        self.assertEqual(part_2(self._pairs), 140)


if __name__ == '__main__':
    main()
