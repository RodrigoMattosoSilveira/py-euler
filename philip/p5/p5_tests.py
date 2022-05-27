import unittest
from philip.p5.p5_helpers import (increment_or_add_to_dict, get_prime_factors,
                                  process_primes_dict, merge_primes_dicts)
from philip.p5.p5 import find_lcm

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

    def test_process_primes_dict(self):
        input_dict = {
            2: 2,
            3: 1,
            5: 2
        }
        self.assertEqual(300, process_primes_dict(input_dict))

    def test_merge_primes_dicts(self):
        master_dict = {}
        input_dict = {
            2: 2,
            3: 1,
            5: 2
        }
        merge_primes_dicts(master_dict, input_dict)
        self.assertEqual(master_dict, input_dict)
        master_dict = {
            2: 3,
            5: 1
        }
        expected_dict = {
            2: 3,
            3: 1,
            5: 2
        }
        merge_primes_dicts(master_dict, input_dict)
        self.assertEqual(master_dict, expected_dict)

    def test_find_lcm(self):
        input_array = [30, 45]
        self.assertEqual(90, find_lcm(input_array))


if __name__ == '__main__':
    unittest.main()
