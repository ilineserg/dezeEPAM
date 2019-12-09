from functools import reduce
import math


def problem9(number=1000):
    """
    Return a product of a, b, c.
    Exists exactly one Pythagorean triplet for which a + b + c = 1000
    a = 2mn;
    b = m**2 − n**2;
    c = m**2 + n**2;
    m > n.
    Input: number - sum of Pythagorean triplet
    """
    return [2 * m * n * (m ** 4 - n ** 4) for m in range(math.ceil(math.sqrt(number // 2))) for n in range(1, m) if
            m * (m + n) == number // 2]


def problem6():
    """
    Return a difference between
    the sum of the squares of the first one hundred natural numbers and
    the square of the sum
    """
    return (lambda a: a[0] ** 2 - a[1])(tuple(sum(x) for x in zip(*[(i, i**2) for i in range(1, 101)])))


def problem48(last_term=1000, last_digits=10):
    """
    Return last ten(last_digits) digits of the series 1**1 + 2**2 + 3**3 + ... + last_term**last_term.

    """
    return str(sum([i ** i for i in range(1, last_term + 1)]))[-last_digits::]


def problem40(max_length=1000000, indexes=(1, 10, 100, 1000, 10000, 100000, 1000000)):
    """
    Return value of expression d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000],
    where d[n] represents the n-th digit of of the fractional part of irrational decimal
    created by concatenating the positive integers.
    """
    series_of_problem40 = ''.join(str(i) for i in range(max_length + 1))
    return reduce(lambda a, x: int(a) * int(x), [series_of_problem40[i] for i in indexes])


print('problem9 - ', problem9())
print('problem6 - ', problem6())
print('problem48 - ', problem48())
print('problem40 - ', problem40())
