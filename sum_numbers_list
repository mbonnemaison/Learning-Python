"""
def list_sum(numbers):
Return the sum of all the items in a list
list_sum([]) = 0
list_sum([1,4,3]) = 8
list_sum([4,3,1]) = 8
raise Exception("TODO")
"""

def list_sum(numbers):
    add_items = 0
    for items in numbers:
        if not (isinstance(items,int) or isinstance(items,float)):
            raise TypeError("expected int or float, got {}".format(type(items)))
        if isinstance(items, bool):
            raise TypeError("expected int or float, got {}".format(type(items)))
        else:
            add_items = add_items + items
    print(add_items)

#Examples to test the code above:
list_test_cases = [[], [1,4,3], ["Matt", 1,2,3,4], [23,34], [True, 34]]
for x in list_test_cases:
    try:
        list_sum(x)
    except TypeError as e:
        print (e)

