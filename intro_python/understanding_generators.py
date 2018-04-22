import math

def get_primes(input_list):
    results_list = list()
    for element in input_list:
        if is_prime(element):
            results_list.append()

def get_primes_two(input_list):
    list_of_primes = [x for x in input_list if is_prime(x)]
    return list_of_primes

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False