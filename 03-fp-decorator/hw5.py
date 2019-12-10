import math
from collections import Counter
import time


c = Counter()
b = Counter()


def profiling_decorator(counter):
    def time_decorator(f):
        def wrapper(*args, **kwargs):
            start = time.clock()
            f(*args, **kwargs)
            stop = time.clock()
            current_time = stop - start
            counter['count_' + f.__name__] += 1
            counter['full_time_' + f.__name__] += current_time
            return f(*args, **kwargs)
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
    for __ in range(n):
        a, b = b, a + b
    return a


def pow(x, n, I, mult):
    """
    Возвращает x в степени n. Предполагает, что I – это единичная матрица, которая
    перемножается с mult, а n – положительное целое
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
    """Возвращает единичную матрицу n на n"""
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


print('fib_1')
print(fib_1(15))
print('Times to start', c['count_fib_1'])
print('Time to run', round(c['full_time_fib_1'], 10))


print('\nfib_2')
print(fib_2(15))
print('Times to start', c['count_fib_2'])
print('Time to run', round(c['full_time_fib_2'], 10))


print('\nfib_3')
print(fib_3(15))
print('Times to start', c['count_fib_3'])
print('Time to run', round(c['full_time_fib_3'], 10))

print('\nfib_4')
print(fib_4(15))
print('Times to start', c['count_fib_4'])
print('Time to run', round(c['full_time_fib_4'], 10))

print('\nfib_5')
print(fib_5(15))
print('Times to start', c['count_fib_5'])
print('Time to run', round(c['full_time_fib_5'], 10))

print(c)
