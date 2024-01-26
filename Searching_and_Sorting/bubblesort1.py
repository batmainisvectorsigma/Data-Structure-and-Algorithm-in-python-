# This the actual program the actual understanding is given below
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

# output
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
"""
This is the explaination to tell you how the program is flowing
"""

def bubbleSort(alist):
    count = 0
    somelist = []
    # 8 times first loop 9-1 =8 9 is the length of the list
    #means loop will run n-1 times that is 9-1 = 8
    for passnum in range(len(alist)-1,0,-1): 
        somelist.append(passnum)
        for i in range(passnum):
            count = count + 1
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return count,somelist
alist = [54,26,93,17,77,31,44,55,20]
print(bubbleSort(alist))
print(alist)

# from here you can see how the program is flowing
#(36, [8, 7, 6, 5, 4, 3, 2, 1])
#[17, 20, 26, 31, 44, 54, 55, 77, 93]
