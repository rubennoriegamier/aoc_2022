from unittest import TestCase, main

from day_25 import part_1


class TestDay25(TestCase):
    _snafu_numbers: list[str]

    @classmethod
    def setUpClass(cls):
        cls._snafu_numbers = ['1=-0-2',
                              '12111',
                              '2=0=',
                              '21',
                              '2=01',
                              '111',
                              '20012',
                              '112',
                              '1=-1=',
                              '1-12',
                              '12',
                              '1=',
                              '122']

    def test_part_1(self):
        self.assertEqual(part_1(self._snafu_numbers), '2=-1=0')


if __name__ == '__main__':
    main()
