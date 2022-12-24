from typing import Callable
from unittest import TestCase, main

from day_21 import parse_jobs, part_1, part_2


class TestDay21(TestCase):
    _jobs: dict[str, int | tuple[Callable[[int, int], int], str, str]]

    @classmethod
    def setUpClass(cls):
        cls._jobs = parse_jobs('''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32''')

    def test_part_1(self):
        self.assertEqual(part_1(self._jobs), 152)

    def test_part_2(self):
        self.assertEqual(part_2(self._jobs), 301)


if __name__ == '__main__':
    main()
