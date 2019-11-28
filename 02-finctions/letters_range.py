def letters_range(start=None, stop=None, step=1, **kwargs):
    if stop is None:
        start, stop = "a", start
    return [kwargs.get(chr(i), chr(i)) for i in range(ord(start), ord(stop), step)]
