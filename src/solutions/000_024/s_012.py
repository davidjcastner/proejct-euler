# Highly divisible triangular number
# Problem 12
# https://projecteuler.net/problem=12

# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred
# divisors?

from src.lib.factors import factorize
from src.lib.triangle import nth_triangle_number


def nth_triangle_divisor_count(n: int) -> int:
    '''returns the numbers of divisors for the nth triangle number'''
    # because triangle numbers = n * (n + 1) // 2,
    # either n or n + 1 will be even, and then can be evenly divided by two
    # both parts can be factorized to speed up process instead of
    # using the larger number
    if n % 2 == 0:
        fact = factorize(n // 2) * factorize(n + 1)
    else:
        fact = factorize(n) * factorize((n + 1) // 2)
    return fact.divisor_count()


def solve(divisor_count: int = 500) -> str:
    '''Problem 12 - Highly divisible triangular number'''
    n = 1
    while nth_triangle_divisor_count(n) <= divisor_count:
        n += 1
    return str(nth_triangle_number(n))


def test_simplified_version() -> None:
    answer = solve(divisor_count=5)
    assert type(answer) == str
    assert answer == '28'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '76576500'


if __name__ == '__main__':
    print(solve())
