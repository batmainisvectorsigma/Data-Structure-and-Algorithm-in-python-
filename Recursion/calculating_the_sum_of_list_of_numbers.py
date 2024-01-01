#CALCULATING THE SUM OF LIST OF NUMBER

#SOLVING USING FOR OR WHILE LOOP
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum
print(listsum([1,3,5,7,9]))

#SOLVING WITHOUT USING FOR OR WHILE LOOP
def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))

#output 
# 25
# 25
