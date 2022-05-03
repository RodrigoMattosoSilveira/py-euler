

def compute_digits_sum(my_number):
    my_string = str(my_number)
    my_sum = 0
    for element in range(0, len(my_string)):
        my_sum += int(my_string[element])
    return my_sum


def get_last_digit(my_number):
    my_string = str(my_number)
    return int(my_string[len(my_string) - 1])


def get_multiples_of_three(_upper_limit):
    multiples_of_three = []
    for i in range(0, _upper_limit):
        # [Is 3 a dividend]
        aux = i
        while aux > 9:
            aux = compute_digits_sum(aux)
        if aux == 3 or aux == 6 or aux == 9:
            multiples_of_three.append(i)

    print(multiples_of_three)
    return multiples_of_three


def get_multiples_of_five(_upper_limit):
    multiples_of_five = []
    for i in range(0, _upper_limit):
        aux = get_last_digit(i)
        if aux == 0 or aux == 5:
            multiples_of_five.append(i)

    print(multiples_of_five)
    return multiples_of_five


def get_multipliers_sum(_upper_limit):
    multipliers_sum = sum(get_multiples_of_three(_upper_limit))
    multipliers_sum = multipliers_sum + sum(get_multiples_of_five(_upper_limit))
    return multipliers_sum


def get_multipliers_sum_xor(_upper_limit):
    my_sum = 0
    my_dividends = []
    for i in range(1, _upper_limit):
        # [Is 3 a dividend]
        aux = i
        while aux > 9:
            aux = compute_digits_sum(aux)
        if aux == 3 or aux == 6 or aux == 9:
            my_sum += i
            my_dividends.append(i)
        else:
            # [Is 5 a dividend]
            aux = get_last_digit(i)
            if aux == 0 or aux == 5:
                my_dividends.append(i)
                my_sum += i

    print(my_dividends)
    return my_sum


def is_last_digit_in_list(x):
    x_in_list = False
    last_digit = get_last_digit(x)
    if last_digit in [0, 2, 4, 5, 6, 8]:
        x_in_list = True
    return x_in_list


def is_three_a_factor(_x):
    three_is_a_factor = False
    aux = _x
    while aux > 9:
        aux = compute_digits_sum(aux)
    if aux == 3 or aux == 6 or aux == 9:
        three_is_a_factor = True
    return three_is_a_factor


def is_any_prime_a_factor(_x, primes):
    a_prime_is_a_factor = False
    for prime in primes:
        if prime != 1:
            if _x % prime == 0:
                a_prime_is_a_factor = True
                break
    return a_prime_is_a_factor


def is_number_prime(_x, _primes):
    number_is_prime = True
    # print('is_number_prime - %s.' % _x)

    if _x != 1 and _x != 2 and _x != 3 and _x != 5:
        number_is_prime = not is_last_digit_in_list(_x)
        number_is_prime = number_is_prime and (not is_last_digit_in_list(_x))
        number_is_prime = number_is_prime and (not is_any_prime_a_factor(_x, _primes))
    return number_is_prime


# https://www.kdnuggets.com/2020/01/python-string-processing-primer.html
# See item #10
def is_palindrome(pn):
    s = str(pn)
    reverse = s[::-1]
    if s == reverse:
        return True
    return False


def build_palindromic_numbers(start, end):
    # print('Building palindromic number between %s  and %s' % (start, end))
    palindromic_numbers = []
    for i in range(end, (start - 1), -1):
        # print('Examining %s ' % i)
        if  is_palindrome(i):
            palindromic_numbers.append(i)
    return palindromic_numbers


def find_palindromic_with_factor_3_digits_long(palindromic_numbers):
    response = -1
    for pn in palindromic_numbers:
        for first_factor in range(100, 1000):
            if pn % first_factor == 0:
                second_factor = int(pn / first_factor)
                if second_factor < first_factor:
                    break
                else:
                    second_factor_len =  len(str(second_factor))
                    if second_factor_len == 3:
                        response = pn
        if response > -1:
            break
    return response

