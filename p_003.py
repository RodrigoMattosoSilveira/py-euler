import os
import sys
import math


script_dir = os.path.dirname(__file__)
helper_dir = os.path.join( script_dir, 'helper')
sys.path.append(helper_dir)
import functions as f


'''
THE PROBLEM
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?

THE ALGORITHM
A01 [get target number] tn <-- agr[1]
A02 [define primes collection] primes <-- []
A03 [define factors collection] factors <-- []
A04 [done when tn is 1] if tn == 1  factors.append(1), DONE
A05 [calculate target number square root] tn_sqr = square_root(tn)
A06 [Find primes between 1 and target number square root] primes = primes_between(1, tn_sqr)
A07 [Fine primes that are factors of tn] factors = prime_factors(primes, tn)
A08 [Highest prime factor is last element added to factors] highest_prime_factor = factors(length(factors)-1]

IS PRIME X
If the number is divisible by any of the prime numbers less than its square root, it is not a prime number; otherwise, 
it is prime.

B01 [assume X is prime] is_prime <-- TRUE
B02 [are any of the primes elements a factor of X]
    B03 [If so, we are done]  is_prime <--  FALSE, BREAK if (X % prime == 0) == 0 else is_prime
B04 [return is_prime] [return is_prime
'''

primes = []
factors = []


def is_number_prime(_x):
    number_is_prime = True
    # print('is_number_prime - %s.' % _x)
    last_digit = f.get_last_digit(x)

    if _x != 1 and _x != 2 and _x != 3 and _x != 5:
        if last_digit == 0 or \
                last_digit == 2 or \
                last_digit == 4 or \
                last_digit == 5 or \
                last_digit == 6 or \
                last_digit == 8:
            number_is_prime = False
        else:
            # [Is 3 a dividend]
            aux = _x
            while aux > 9:
                aux = f.compute_digits_sum(aux)
            if aux == 3 or aux == 6 or aux == 9:
                number_is_prime = False
            else:
                for prime in primes:
                    if prime != 1:
                        if _x % prime == 0:
                            number_is_prime = False
                            break
    return number_is_prime


target = int(sys.argv[1])
print(' What is the largest prime factor of the number %s.' % target)

target_sqr = int(math.sqrt (target))
for x in range (1, target_sqr + 1):
    if is_number_prime(x):
        print('%s is prime' % x)
        primes.append(x)
        if target % x == 0:
            factors.append(x)

if len(factors) == 1:
    factors.append(target)
print('Factors %s.' % factors)
print('Highest prime factor of %s is %s' % (target, factors[len(factors) - 1]))

