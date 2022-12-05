from unittest import TestCase, main

from day_05 import Part, parse_stacks, parse_steps, part_


class TestDay05(TestCase):
    _stacks: list[list[str]]
    _steps: list[tuple[int, int, int]]

    def setUp(self):
        self._stacks = parse_stacks('''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3''')
        self._steps = parse_steps('''move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2''')

    def test_part_1(self):
        self.assertEqual(part_(Part.ONE, self._stacks, self._steps), 'CMZ')

    def test_part_2(self):
        self.assertEqual(part_(Part.TWO, self._stacks, self._steps), 'MCD')


if __name__ == '__main__':
    main()
