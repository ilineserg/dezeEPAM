def collatz_steps(n, step=0):
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        step += 1
    return step


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(27) == 111
assert collatz_steps(1000) == 111
assert collatz_steps(10000000000000000000000000000000000000000000000000000000000) == 348