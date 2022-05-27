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
Create an empty dictionary
For each natural number in the input array:
1. Find the prime factors
2. Store the prime factors in the dictionary (declared outside the loop) where each prime factor is a key
   and its # of occurrences is the value
    2a. Only store the prime factor if either 1) its key is not already in the dict or 2) its value is greater
        than the existing value stored in the dict
'''