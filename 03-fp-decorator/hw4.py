def applydecorator(f_saymyname):
    def wrapper(f_foo):
        def inner(*args, **kwargs):
            return f_saymyname(f_foo, *args, **kwargs)
        return inner
    return wrapper


@applydecorator
def saymyname(f, *args, **kwargs):
    print('Name is', f.__name__)
    return f(*args, **kwargs)


# saymyname is now a decorator
@saymyname
def foo(*whatever):
    return whatever


print(*foo(40, 2))