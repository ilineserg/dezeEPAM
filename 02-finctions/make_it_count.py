counter_name = 0


def func():
    print("You call func!")


def make_it_count(function, counter_n):
    def new_func():
        globals()[counter_n] += 1
        function()

    return new_func