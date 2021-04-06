def fib(n):
    if n < 1:
        return[0]
    if n == 1:
        return[0, 1]
    A = fib(n - 1)
    return A + [A[-1] + A[-2]]

print(fib(5)) #[0, 1, 1, 2, 3, 5]
print(fib(5)[-1]) #5