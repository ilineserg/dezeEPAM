import inspect


def any_foo(*args, **kwargs):
    print("This is SPARTA!")


def modified_func(func, *fixated_args, **fixated_kwargs):
    def inner(*args, **kwargs):
        new_args = ()
        args_in_doc = None
        kwargs_in_doc = None
        if args:
            new_args = fixated_args + args
        if kwargs:
            fixated_kwargs.update(kwargs)
        frame = inspect.currentframe()
        values = inspect.getargvalues(frame)
        if "new_args" in values[3]:
            if args_in_doc is None:
                args_in_doc = values[3].get("new_args")
        if "fixated_kwargs" in values[3]:
            if kwargs_in_doc is None:
                kwargs_in_doc = values[3].get("fixated_kwargs")

        inner.__name__ = "func_{}".format(func.__name__)
        inner.__doc__ = """A func implementation of {} with pre-applied arguments being: \n\nargs: {}, kwargs {} 
        \nsource_code:\n{}""".format(
            inner.__name__, args_in_doc, kwargs_in_doc, inspect.getsource(func)
        )
        return func(*new_args, **fixated_kwargs)

    return inner


if __name__ == "__main__":
    a = modified_func(any_foo, 1, 2, 3, a=1, b=90)
    a(3, 4, 5, b=2, c=3)
    print(a.__doc__)
