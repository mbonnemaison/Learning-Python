"""
def list_contains(my_list, item):
Return True if `item` is in `my_list`; return False otherwise
list_contains([], 3) = False
list_contains([2,4], 3) = False
list_contains([42, 3], 3) = True
list_contains([3,3,3], 3) = True
raise Exception("TODO")
"""

def list_contains(my_list, item):
    for i in my_list:
        if item in my_list:
            print(True)
            break
        else:
            print(False)

#Examples to test the code above:
list_contains([], 3)
list_contains([2,4], 3)
list_contains([42, 3], 3)
list_contains([3,3,3], 3)
