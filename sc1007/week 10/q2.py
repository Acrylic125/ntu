import time

def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_iterative(n-2)

def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

test = [1, 10, 20, 30, 40, 45]
for v in test:
    start = time.perf_counter()
    res = fib_recursive(v)
    end = time.perf_counter()
    print(f"Recursive fib({v}) timing: {end - start:.4f} seconds = {res}")
    start = time.perf_counter()
    res = fib_iterative(v)
    end = time.perf_counter()
    print(f"Iterative fib({v}) timing: {end - start:.4f} seconds = {res}")
    print()

