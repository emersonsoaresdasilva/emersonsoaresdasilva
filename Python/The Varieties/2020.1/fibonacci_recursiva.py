def fib(n):
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)
def fib_2(n):
    return 1 if n <= 2 else fib(n-1) + fib(n-2)
