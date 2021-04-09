"""
def list_all(booleans):
Return True if every item in the list is True; otherwise return False
list_all([]) = True
list_all([True]) = True
list_all([False]) = False
list_all([True, False, True]) = False
raise Exception("TODO")
"""

def list_all(booleans):
    for bools in booleans:
        if not isinstance(bools, bool):
            raise TypeError("expected bool, got {}".format(type(bools)))
    if False not in booleans:
        print(True)
    else:
        print(False)

#Examples to test the code above:
list_all_test_cases = [[], [True], [False], [True, False, True], [True, True], ["Matt", "Mathilde"], [23, 4.3]]
for x in list_all_test_cases:
    try:
        list_all(x)
    except TypeError as e:
        print(e)
