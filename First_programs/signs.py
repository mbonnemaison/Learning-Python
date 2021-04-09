"""
Instructions:
def sign(n):

    Return the 'sign' of the number as a string
    sign(-5) = "-"
    sign(0) = "0"
    sign(18) = "+"
    
    raise Exception("TODO")
"""

def sign(n):
    if not (isinstance(n, int) or isinstance(n, float)):
        raise TypeError("expected int or float, got {}".format(type(n)))
    if n == 0:
        print("0")
    elif n > 0:
        print("+")
    else:
        print("-")

sign_test_cases = [9, 0, -4, 4.5, "Matt"]
for x in sign_test_cases:
    try:
        sign(x)
    except TypeError as e:
        print(e)
