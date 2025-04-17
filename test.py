def fib(x):
    if x < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)
    


fib(6)