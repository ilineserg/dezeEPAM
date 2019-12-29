""""
Реализовать контекстный менеджер, который подавляет переданные исключения
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
"""


class Suppressor:

    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        print(f'Exit exception text: {exc_value}')
        return issubclass(exc_type, self.exceptions)


if __name__ == '__main__':
    with Suppressor(ZeroDivisionError):
        a1 = 1 / 0
    print("It's fine")

    with Suppressor(TypeError):
        b1 = 35 + 'qwe'
    print("It's fine")

    with Suppressor(TypeError, ZeroDivisionError):
        a2 = 1 / 0
        b2 = 35 + 'qwe'
    print("It's fine")

    with Suppressor(TypeError, ZeroDivisionError):
        b3 = 35 + 'qwe'
        a3 = 1 / 0
    print("It's fine")