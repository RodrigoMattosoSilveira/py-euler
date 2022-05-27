'''
Problem 5

    https://projecteuler.net/problem=5

Problem Statement 

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

IOCE
I - array of numbers
O - LCM of inputted array
C - None
E - given an empty array, or an array containing non-natural numbers, should return None

Strategy
To find the LCM of a set of numbers, you can first find the prime factors of each number. Then multiply all factors with
each being raised to the power of the greatest number of times it occurs in any number.

Example
To find the LCM of 30 and 45, first list the prime factors of each number:
30 = 2 x 3 x 5
45 = 3 x 3 x 5
Therefore:
LCM = 2 x 3^2 x 5 = 90

Algorithm
Create an empty dictionary to store primes
For each natural number in the input array:
1. Find the prime factors
2. Store the prime factors in the dictionary (declared outside the loop) where each prime factor is a key
   and its # of occurrences is the value
    2a. Only store the prime factor if either 1) its key is not already in the dict or 2) its value is greater
        than the existing value stored in the dict
3. Repeat 2 and 2a against the master primes dictionary
4. After looping through all numbers in the input array, process the master dictionary by multiplying all of its
   keys against each other raised to the power of their value
5. Return the value from 4

'''
from philip.p5.p5_helpers import (get_prime_factors, process_primes_dict, merge_primes_dicts)


def find_lcm(array: list) -> int:
    master_primes_dict = {}
    for num in array:
        primes_dict = get_prime_factors(num)
        merge_primes_dicts(master_primes_dict, primes_dict)
    return process_primes_dict(master_primes_dict)


input_array = []
for i in range(1, 20):
    input_array.append(i)
print(find_lcm(input_array))
