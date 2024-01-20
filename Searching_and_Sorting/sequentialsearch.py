"""
This is a simple solution to find a item in list
I will explain it in analysis which is given below"
"""
def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))

"""
OUTPUT
False
True
"""


"""
     ALGORITHM ANALYSIS
complexity is O(n)
case                Best Case         Worst Case            Average Case
item is present       1                  n                      n/2
item is not present   n                  n                       n
"""




"""
    IF THE LIST IS IN ASCENDING ORDER OR IN ANY OTHER WHAT THINGS CAN BE DONE 
"""

def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))

"""
OUTPUT
False
True
"""
