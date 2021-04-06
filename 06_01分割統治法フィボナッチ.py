def fib(n):
    if n < 2:
        return n
    else:
        a = fib(n - 1) #再帰的定義
        b = fib(n - 2)
        c = a + b
        return c

print(fib(5)) #この場合返り値cがあるので、ターミナルに表示するにはprintが必要
