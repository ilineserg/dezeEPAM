"""
Реализовать класс Quaternion, позволяющий работать с кватернионами
https://ru.wikipedia.org/wiki/%D0%9A%D0%B2%D0%B0%D1%82%D0%B5%D1%80%D0%BD%D0%B8%D0%BE%D0%BD
Функциональность (магическими методами):
- сложение
- умножение
- деление
- сравнение
- нахождение модуля
- строковое представление и repr
По желанию:
- взаимодействие с числами других типов
"""


class Quaternion:

    def __init__(self, s=0, x=0, y=0, z=0):
        self.s = s
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Quaternion):
            return Quaternion(s=self.s + other.s,
                              x=self.x + other.x,
                              y=self.y + other.y,
                              z=self.z + other.z)
        if isinstance(other, (int, float)):
            return self + Quaternion(other)

    def __iadd__(self, other):
        return self + other

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, Quaternion):
            return Quaternion(s=self.s * other.s - self.x * other.x - self.y * other.y - self.z * other.z,
                          x=self.s * other.x + other.s * self.x + self.y * other.z - other.y * self.z,
                          y=self.s * other.y + other.s * self.y + self.z * other.x - other.z * self.x,
                          z=self.s * other.z + other.s * self.z + self.x * other.y - other.x * self.y)
        if isinstance(other, (int, float)):
            return self * Quaternion(other)

    def __imul__(self, other):
        return self * other

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, Quaternion):
            return self * other.inverse()
        if isinstance(other, (int, float)):
            return self / Quaternion(other)

    def __itruediv__(self, other):
        return self / other

    def __rtruediv__(self, other):
        return self / other

    def __eq__(self, other):
        if isinstance(other, Quaternion):
            return self.__abs__() == other.__abs__()
        if isinstance(other, (int, float)):
            return self.__eq__(Quaternion(other))

    def __ne__(self, other):
        if isinstance(other, Quaternion):
            return self.__abs__() != other.__abs__()
        if isinstance(other, (int, float)):
            return self.__ne__(Quaternion(other))

    def __lt__(self, other):
        if isinstance(other, Quaternion):
            return self.__abs__() < other.__abs__()
        if isinstance(other, (int, float)):
            return self.__lt__(Quaternion(other))

    def __le__(self, other):
        if isinstance(other, Quaternion):
            return self.__abs__() <= other.__abs__()
        if isinstance(other, (int, float)):
            return self.__le__(Quaternion(other))

    def __gt__(self, other):
        if isinstance(other, Quaternion):
            return self.__abs__() > other.__abs__()
        if isinstance(other, (int, float)):
            return self.__gt__(Quaternion(other))

    def __ge__(self, other):
        if isinstance(other, Quaternion):
            return self.__abs__() >= other.__abs__()
        if isinstance(other, (int, float)):
            return self.__ge__(Quaternion(other))

    def __abs__(self):
        return self.sum_of_squares()**(1/2)

    def __str__(self):
        return f'{self.s:.3f}{self.x:+.3f}i{self.y:+.3f}j{self.z:+.3f}k'

    def __repr__(self):
        return f'Quaternion({repr(self.s)}, {repr(self.x)}, {repr(self.y)}, {repr(self.z)})'

    def vector_conjugate(self):
        return Quaternion(s=self.s, x=-self.x, y=-self.y, z=-self.z)

    def sum_of_squares(self):
        return sum((self.s**2, self.x**2, self.y**2, self.z**2))

    def inverse(self):
        ss = self.sum_of_squares()
        vc = self.vector_conjugate()
        return Quaternion(s=vc.s / ss, x=vc.x / ss, y=vc.y / ss, z=vc.z / ss)


if __name__ == '__main__':
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(4, 3, 2, 1)
    print(q1 + q2, 'is +')
    print(q1 * q2, 'is *')
    print(q2 / q1, 'is /')
    print('\n')
    print(q1 > q2, 'is >')
    print(q1 >= q2, 'is >=')
    print(q1 < q2, 'is <')
    print(q1 <= q2, 'is <=')
    print(q1 == q2, 'is ==')
    print(q1 != q2, 'is !=')
    print('\n')
    print(abs(q1), abs(q2), 'is abs')
    print(str(q2), 'is str')
    print(repr(q2), 'is repr')
    print(str(q2/q1))

