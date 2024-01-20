"""
Use this algorithm when it is in ascending order
"""

"""
      SOLUTION
"""

def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint + 1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

"""
    EXPLAINATION
    WE FIND THE MID AND CHECK WHETHER IT IS THE ITEM OR NOT
    AND WE WILL AGAIN KEEP BREAKING THE LIST UNTIL AND UNLESS WE DON'T GET THAT ITEM
"""
