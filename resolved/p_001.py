import os
import sys

script_dir = os.path.dirname( __file__ )
helper_dir = os.path.join( script_dir, '..', 'helper')
sys.path.append(helper_dir)
import functions as f

upper_limit = int(sys.argv[1])
print('Find the sum of all the multiples of 3 or 5 below %s.' % upper_limit)

'''
Algorithm
    Divisible by 3 - When the sum of a natural integer's digits is 3, 6, or 9, it is divisible by 3; if the sum is 
    greater than 10, compute the sum of the sum's digits, and repeat until we have a sum that is lower than 10;
    Divisible by 5 - hen a natural's number last digit is 0 or 5, it is divisible by 5;
        T0: [host the dividends] dividends <-- []
        T1: [Inspect numbers between 1 and upper_limit, in i] candidate <-- i
            T2: [Is 3 a dividend]
                T3: [initialize] aux <-- i
                T4: [repeat until digits sum < 10] while sum <-- compute_digits_sum(aux) < 10
                    aux <-- sum
                T5: [Is dividend if sum 3, 6, or 9]  If (sum == 3 | sum == 6 | sum == 9] then dividends.append(i)
                T5A: [only one dividend] If (sum == 3 | sum == 6 | sum == 9] then break
            T6: [Is 5 a dividend]
                 T7: [initialize] aux <-- i
                 T8: [inspect last digit] d <-- last_digit(i)
                 T9: [Is dividend if last digit 0, 5]  If (d == 0 | d == 5) then then dividends.append(i)
        T10: [compute_digits_sum]
            T10: [cast as string] string_name = ste(arg_1)
            T11: [initialize sum to zero] sum <-- 0
            T12: [add digits] for element in range(0, len(string_name)): sum <-- sum + int(element)
            T13: [return sum] 
        T14: [get last digit]
             T10: [cast as string] string_name = str(arg_1)
             T10: [return last digit] string_name = int(string_name(len(string_name) - 1)    
'''

# multiplier_sum = f.get_multipliers_sum(upper_limit)
multiplier_sum = f.get_multipliers_sum_xor(upper_limit)
print('sum of all the multiples of 3 or 5 below %s = %s' % (upper_limit, multiplier_sum))
