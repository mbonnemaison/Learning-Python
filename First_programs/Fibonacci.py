"""
def fibonacci(n):
The fibonacci sequence is:
F0 = 0
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
and so on, where F(N) = F(N-2) + F(N-1)
raise Exception("TODO")
"""

def fibonacci(n):
    if not isinstance(n,int):
        raise TypeError ("expected int, got {}".format(type(n)))
    if n < 0:
        raise TypeError ("expected positive int, got {}".format(n))
    if isinstance(n,bool):
        raise TypeError ("expected int, got {}".format(type(n)))
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibo_one = 1
        fibo_two = 0
        while n > 1:
            fibo = fibo_two + fibo_one
            fibo_two = fibo_one
            fibo_one = fibo
            n = n - 1
        return fibo

#Examples to test the code above:
fibonacci_test_cases = [0, 8, 4.3, -2, True]
for x in fibonacci_test_cases:
    try:
        print(fibonacci(x))
    except TypeError as e:
        print(e)

