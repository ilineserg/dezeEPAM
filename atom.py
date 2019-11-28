def uno(n):
    return n + 1


def dos(n):
    return n + 2


def tress(n):
    return n + 3


def atom(value=None):
    holder = lambda: None

    setattr(holder, 'secret', value)

    def get_value():
        return getattr(holder, 'secret', None)

    def set_value(new_value):
        setattr(holder, 'secret', new_value)

    def process_value(*args):
        for arg in args:
            set_value(arg(get_value()))

    def del_value():
        delattr(holder, 'secret')

    return get_value, set_value, process_value, del_value

