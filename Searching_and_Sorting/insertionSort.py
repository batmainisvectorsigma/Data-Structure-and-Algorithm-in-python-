def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

"""
 OUTPUT
[17, 20, 26, 31, 44, 54, 55, 77, 93]

  EXPLAINATION
when n = 3 or index = 3 
all the items from index 3 to below that is 
4 items gets sorted that is 54 26 93 17 is sorted 

IN MORE DETAIL EXPLAINATION
index = 3
currentvalue = 17
position = 3

first loop 
93 > 17
index 3 = 93
position = 2

second loop 
54 > 17
index 2 = 93
position = 1

third loop 
26 > 17
index 1 = 26
position = 0

alist[0] = 17 that is
index 0 = 17

the whole table
index 0   index 1 index 2  index 3
17          26      54       93
"""
