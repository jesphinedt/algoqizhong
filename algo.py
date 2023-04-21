import random
import time

def linear_search(S, x):
    for i in range(len(S)):
        if S[i] == x:
            return True
    return False

def binary_search(S, x):
    low, high = 0, len(S) - 1
    while low <= high:
        mid = (low + high) // 2
        if S[mid] == x:
            return True
        elif S[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

def fibonacci_search(S, x):
    def fibonacci_gen():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    fib_gen = fibonacci_gen()
    fib1, fib2 = next(fib_gen), 0
    offset = -1
    while fib1 > 1:
        i = min(offset+fib2, len(S)-1)
        if S[i] < x:
            fib1, fib2 = fib2, fib1 - fib2
            offset = i
        elif S[i] > x:
            fib1, fib2 = fib1 - fib2, fib2
        else:
            return True
    if fib1 and S[offset+1] == x:
        return True
    return False

# Perform the experiments
for n in range(10, 1010, 10):
    S = [random.randint(0, 10000) for _ in range(n)]
    x = random.randint(0, 10000)

    print(f"n={n}:")

    # Linear search
    linear_times = []
    for i in range(5):
        start = time.perf_counter()
        linear_search(S, x)
        end = time.perf_counter()
        linear_times.append(end - start)
    print(f"Linear search: {sum(linear_times)/len(linear_times)}")

    # Binary search
    S.sort()
    binary_times = []
    for i in range(5):
        start = time.perf_counter()
        binary_search(S, x)
        end = time.perf_counter()
        binary_times.append(end - start)
    print(f"Binary search: {sum(binary_times)/len(binary_times)}")

    # Fibonacci search
    fibonacci_times = []
    for i in range(5):
        start = time.perf_counter()
        fibonacci_search(S, x)
        end = time.perf_counter()
        fibonacci_times.append(end - start)
    print(f"Fibonacci search: {sum(fibonacci_times)/len(fibonacci_times)}")

    print()
