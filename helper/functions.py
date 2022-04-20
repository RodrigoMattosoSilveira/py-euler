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
