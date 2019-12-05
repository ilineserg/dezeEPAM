import datetime
from functools import reduce


problem9 = [2 * m * n * (m ** 4 - n ** 4) for m in range(334) for n in range(1, m, 2) if
           2 * m ** 2 + 2 * m * n == 1000]


problem6 = sum([i for i in range(1, 101)])**2 - sum([i**2 for i in range(1, 101)])


problem48 = str(sum([i**i for i in range(1, 1001)]))[-10::]
problem482 = sum(map(lambda x: x**x, range(1, 1001)))


series_of_problem40 = ''.join(str(i) for i in range(1000001))
problem40 = reduce(lambda a, x: int(a) * int(x),
                   [series_of_problem40[i] for i in (1, 10, 100, 1000, 10000, 100000, 1000000)])


print('problem9 - ' + str(problem9[0]))
print('problem6 - ' + str(problem6))
print('problem48 - ' + problem48)
print('problem40 - ' + str(problem40))