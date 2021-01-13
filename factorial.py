"""
def factorial(n):
Return n!  (n factorial)
0! = 1
1! = 1
2! = 2 (2 * 1)
3! = 6 (3 * 2 * 1)
4! = 24 (4 * 3 * 2 * 1)
raise Exception("TODO")
Write a function without using range()
"""

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("expected int, got {}".format(type(n)))
    if n < 0:
        raise TypeError("expected a positive value, got {}".format(n))
    if n == 0:
        print(1)
    else:
        fact = 1
        while n > 0:
            fact = fact * n
            n = n - 1
        print(fact)

#Examples to test the code above:
factorial_test_cases = [0, 4, -3, "Matt"]
for x in factorial_test_cases:
    try:
        factorial(x)
    except TypeError as e:
        print(e)
