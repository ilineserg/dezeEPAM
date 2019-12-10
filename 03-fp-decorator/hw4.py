def applydecorator(decorator_func):
    def wrapper(applied_func):
        def inner(*args, **kwargs):
            return decorator_func(applied_func, *args, **kwargs)

        return inner

    return wrapper


@applydecorator
def saymyname(f, *args, **kwargs):
    print("Name is", f.__name__)
    return f(*args, **kwargs)


# saymyname is now a decorator
@saymyname
def foo(*whatever):
    return whatever


print(*foo(40, 2))
