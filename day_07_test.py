from unittest import TestCase, main

from day_07 import part_1_and_2


class TestDay07(TestCase):
    _part_1: int
    _part_2: int

    def setUp(self):
        self._part_1, self._part_2 = part_1_and_2(list(map(str.split, ['$ cd /',
                                                                       '$ ls',
                                                                       'dir a',
                                                                       '14848514 b.txt',
                                                                       '8504156 c.dat',
                                                                       'dir d',
                                                                       '$ cd a',
                                                                       '$ ls',
                                                                       'dir e',
                                                                       '29116 f',
                                                                       '2557 g',
                                                                       '62596 h.lst',
                                                                       '$ cd e',
                                                                       '$ ls',
                                                                       '584 i',
                                                                       '$ cd ..',
                                                                       '$ cd ..',
                                                                       '$ cd d',
                                                                       '$ ls',
                                                                       '4060174 j',
                                                                       '8033020 d.log',
                                                                       '5626152 d.ext',
                                                                       '7214296 k'])))

    def test_part_1(self):
        self.assertEqual(self._part_1, 95_437)

    def test_part_2(self):
        self.assertEqual(self._part_2, 24_933_642)


if __name__ == '__main__':
    main()
