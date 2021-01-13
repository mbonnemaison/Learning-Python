"""
def absolute_value(n):
Return the absolute value of the number
absolute_value(-5) = 5
absolute_value(0) = 0
absolute_value(18) = 18
raise Exception("TODO")
"""

def absolute_value(n):
    if not (isinstance(n, int) or isinstance(n, float)):
        raise TypeError("expected int or float, got {}".format(type(n)))
    if n >= 0:
        print(n)
    else:
        print(-n)

#Examples to test the program above:
absolute_test_cases = [9, 0, -4, "Matt"]
for x in absolute_test_cases:
    try:
        absolute_value(x)
    except TypeError as e:
        print(e)
