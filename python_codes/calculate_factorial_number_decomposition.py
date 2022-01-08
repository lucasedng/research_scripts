from sympy import primerange
from typing import List, Dict
from pprint import pprint


def _prime_number_less_than_n(number: int) -> List[int]:
    return list(primerange(0, number))


def _calculate_vp_n_factorial(number: int, prime: int) -> int:

    vp_n_factorial = 0
    power = 1
    while number//(prime**power):
        vp_n_factorial += number//(prime**power)
        power += 1

    return vp_n_factorial

# returns the power of all prime numbers that are part of the decomposition of n!
def factorial_factoring(number: int) -> str:
    return ''.join(
        f'({prime}^{_calculate_vp_n_factorial(number, prime)})'
        for prime in _prime_number_less_than_n(number)
    )

# returns a dictionary with a prime number and its power in decomposing n!
def factorial_factoring_dict(number: int) -> Dict[int, int]:
    return {
        prime: _calculate_vp_n_factorial(number, prime)
        for prime in _prime_number_less_than_n(number)
    }


print(factorial_factoring(50))
pprint(factorial_factoring_dict(50), width=1)
