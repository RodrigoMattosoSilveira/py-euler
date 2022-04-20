import os
import sys

'''
THE PROBLEM
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?

FINDING IF A NUMBER IS PRIME
How to Tell if a Large Number is Prime?

Check the units place of that number. If it ends with 0, 2, 4, 6 and 8, it is not a prime number. ...
Take the sum of the digits of that number. If the sum is divisible by 3, the number is not a prime number.
After confirming the falsity of steps 1 and 2, find the square root of the given number.
Divide the given number by all the prime numbers below its square root value.
If the number is divisible by any of the prime numbers less than its square root, it is not a prime number; otherwise, it is prime.

THE ALGORITHM
'''

a_number = int(sys.argv[1])
print(' What is the largest prime factor of the number %s.' % a_number)
