from unittest import TestCase, main

from day_11 import MonkeyRules, parse_monkey, part_1, part_2


class TestDay11(TestCase):
    _data: list[tuple[list[int], MonkeyRules]]

    def setUp(self):
        self._data = list(map(parse_monkey, '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''.split('\n\n')))

    def test_part_1(self):
        self.assertEqual(part_1(self._data), 10_605)

    def test_part_2(self):
        self.assertEqual(part_2(self._data), 2_713_310_158)


if __name__ == '__main__':
    main()
