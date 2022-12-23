from unittest import TestCase, main

from day_20 import decrypt


class TestDay20(TestCase):
    _numbers: list[int]

    @classmethod
    def setUpClass(cls):
        cls._numbers = [1, 2, -3, 3, -2, 0, 4]

    def test_part_1(self):
        self.assertEqual(decrypt(self._numbers), 3)

    def test_part_2(self):
        self.assertEqual(decrypt(self._numbers, 811_589_153, 10), 1_623_178_306)


if __name__ == '__main__':
    main()
