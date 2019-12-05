def collatz_steps(n, step=0):
    return step if n == 1 else collatz_steps(n / 2, step + 1) if n % 2 == 0 else collatz_steps(n * 3 + 1, step + 1)


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(27) == 111
assert collatz_steps(1000) == 111
assert collatz_steps(10000) == 29