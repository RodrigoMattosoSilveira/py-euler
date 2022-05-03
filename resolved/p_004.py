import os
import sys

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers. 906609

HIGH LEVEL ALGORITHM
Build a collection of all palindromic numbers consisting of 6 digits
Working backwards, find the first palindrome that has a 3 digit factor
If the 3-digit factor divided into the palindromic number is also a 3-digit number, we are set

Build palindromic numbers collection
A01 [get numbers in the 100 to 999 range] for i in range(100,1000) 
A02 [get their digits] digits <-- str(i)

'''

script_dir = os.path.dirname(__file__)
helper_dir = os.path.join(script_dir, '..', 'helper')
sys.path.append(helper_dir)
import functions as f

number_of_digits = int(sys.argv[1])
print('Find the largest palindrome number made from the product of two %s-digit numbers' % number_of_digits)
palindromic_numbers = f.build_palindromic_numbers(100000, 999999)
palindromic_number = f.find_palindromic_with_factor_3_digits_long(palindromic_numbers)
if palindromic_number > 0:
    print('Palindromic number is %s' % palindromic_number)
else:
    print('Did not find Palindromic number')
