import unittest
from philip.p5.p5_helpers import increment_or_add_to_dict, get_prime_factors


class Problem5TestCase(unittest.TestCase):
    def test_increment_or_add_to_dict(self):
        starting_dict = {
            2: 4,
            3: 1
        }
        # test that it adds new key properly
        increment_or_add_to_dict(starting_dict, 5)
        expected_dict = {
            2: 4,
            3: 1,
            5: 1
        }
        self.assertEqual(expected_dict, starting_dict)

        # test that increments existing key's value properly
        increment_or_add_to_dict(starting_dict, 5)
        expected_dict = {
            2: 4,
            3: 1,
            5: 2
        }
        self.assertEqual(expected_dict, starting_dict)

    def test_get_prime_factors(self):

        expected_dict = {
            3: 2
        }
        self.assertEqual(expected_dict, get_prime_factors(9))

if __name__ == '__main__':
    unittest.main()
