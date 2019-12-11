import math
from collections import Counter
import time


c = Counter()


def profiling_decorator(counter):
    def time_decorator(f):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = f(*args, **kwargs)
            stop = time.time()
            counter[(f.__name__, 'count')] += 1
            counter[(f.__name__, 'full_time')] += stop - start
            return res
        return wrapper
    return time_decorator


@profiling_decorator(c)
def fib_1(n):
    sqrts = math.sqrt(5)
    phi = (sqrts + 1) / 2
    return int(phi ** n / sqrts + 0.5)


@profiling_decorator(c)
def fib_2(n):
    if n > 2:
        return fib_2(n - 1) + fib_2(n - 2)
    else:
        return 1


@profiling_decorator(c)
def fib_3(n):
    M = {0: 0, 1: 1}
    if n in M:
        return M[n]
    M[n] = fib_3(n - 1) + fib_3(n - 2)
    return M[n]


@profiling_decorator(c)
def fib_4(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


def pow(x, n, I, mult):
    """
    Returns x ** n. Suggests that I is unit matrix, which is multiplied with mult and n is positive number.
    """
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = pow(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y


def identity_matrix(n):
    """Returns unit matrix n * n"""
    r = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]


def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b
            for a, b in zip(row_a, col_b))
            for col_b in BT]
            for row_a in A]


@profiling_decorator(c)
def fib_5(n):
    F = pow([[1, 1], [1, 0]], n, identity_matrix(2), matrix_multiply)
    return F[0][1]


def optimal_fibonacci():
    result = None
    temp = 0
    for i in c:
        if i[1] == 'full_time':
            temp = c.get(i)
            if result is None or temp < result[1]:
                result = (i, temp)
    return f'Optimal function Fibonacci by time is: {result[0][0]}.\nFunction runs for: {result[1]} sec.'


if __name__ == '__main__':
    n = 15
    fib_1(n)
    fib_2(n)
    fib_3(n)
    fib_4(n)
    fib_5(n)
    print(optimal_fibonacci())