

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
