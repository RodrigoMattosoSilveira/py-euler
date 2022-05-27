

def get_prime_factors(num: int) -> dict:
    prime_factors = {}
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            increment_or_add_to_dict(prime_factors, i)
    if num > 1:
        increment_or_add_to_dict(prime_factors, num)
    return prime_factors


def increment_or_add_to_dict(dictionary: dict, value: int) -> None:
    if value not in dictionary:
        dictionary[value] = 1
    else:
        dictionary[value] += 1


def process_primes_dict(dictionary: dict) -> int:
    total = 1
    for key in dictionary:
        total *= key ** dictionary[key]
    return total


def merge_primes_dicts(master_dictionary: dict, dictionary: dict) -> None:
    for key in dictionary:
        if key not in master_dictionary:
            master_dictionary[key] = dictionary[key]
        else:
            if dictionary[key] > master_dictionary[key]:
                master_dictionary[key] = dictionary[key]
