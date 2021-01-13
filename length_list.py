"""
def length(xs):
Return the length of the list
length([]) = 0
length([41]) = 1
length([8]) = 1
length([2,2,2,2]) = 4
raise Exception("TODO")
Write a function without using len()
"""

def length(xs):
    if xs == []:
        print(0)
    else:
        count = 0
        for i in xs:
            count = count + 1
        print(count)

#Examples to test the code above:
a = [23, True, 21, 45]
length([])
length([41])
length(a)
