import unittest
from sample_project import find_the_pairs


class TestFindThePairs(unittest.TestCase):
    def test_multiple_pairs(self):
        self.assertEqual(
            find_the_pairs([1, 8, 9, 4, 5, 0, 20, -4, 12, 16, 7], 9),
            {(1, 8), (9, 0), (4, 5)},
        )

    def test_single_pair(self):
        self.assertEqual(find_the_pairs([1, 4, 5, 0, 20, -4, 12, 16, 7], 9), {(4, 5)})

    def test_no_pair(self):
        self.assertEqual(find_the_pairs([1, 4, 0, 20, -4, 12, 16, 7], 9), set())

    def test_empty_list(self):
        self.assertEqual(find_the_pairs([], 9), set())

    def test_single_input_number(self):
        self.assertEqual(find_the_pairs([2], 5), set())

    def test_target_zero(self):
        self.assertEqual(find_the_pairs([5, 4, -3, 2, 1, 0, 3], 0), {(-3, 3)})


if __name__ == "__main__":
    unittest.main()
