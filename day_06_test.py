from unittest import TestCase, main

from day_06 import part_1_and_2


class TestDay06(TestCase):
    _data: list[str]

    def setUp(self):
        self._data = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb',
                      'bvwbjplbgvbhsrlpgdmjqwftvncz',
                      'nppdvjthqldpwncqszvftbrmjlhg',
                      'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
                      'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']

    def test_part_1(self):
        for i, (data, result) in enumerate(zip(self._data, [7, 5, 6, 10, 11])):
            with self.subTest(i=i):
                self.assertEqual(part_1_and_2(data, 4), result)

    def test_part_2(self):
        for i, (data, result) in enumerate(zip(self._data, [19, 23, 23, 29, 26])):
            with self.subTest(i=i):
                self.assertEqual(part_1_and_2(data, 14), result)


if __name__ == '__main__':
    main()
