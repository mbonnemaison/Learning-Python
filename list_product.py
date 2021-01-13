"""
def list_product(numbers):
Return the product of all the items in a list
list_product([]) = 1
list_product([1,4,3]) = 12
list_product([4,3,1]) = 12
raise Exception("TODO")
"""

def list_product(numbers):
    if numbers == []:
        print(1)
    else:
        product = 1
        for i in numbers:
            if not (isinstance(i,float) or isinstance(i,int)):
                raise TypeError("expected int or float, got {}".format(type(i)))
            if isinstance(i, bool):
                raise TypeError("expected int or float, got {}".format(type(i)))
            product = product * i
        print(product)

#Examples to test the code above:
product_test_cases = [[1,4,3], [], ["Matt", 34, True],[23, 4,3], [23, 4,3, False]]
for test in product_test_cases:
    try:
        list_product(test)
    except TypeError as e:
        print(e)
