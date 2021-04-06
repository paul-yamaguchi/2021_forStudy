def fib(n):
    A = [None] * (n + 1)
    A[0] = 0
    A[1] = 1
    for i in range(2, n + 1):
        A[i] = A[i - 1] + A[i - 2]
    return A[n]

print(fib(5))
