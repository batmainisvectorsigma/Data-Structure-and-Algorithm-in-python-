#CONVERT AN INTEGER TO STRING TO ANY BASE
#HERE WE ARE CONVERTING IT INTO HEXADECIMAL 
def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16))
print(toStr(145,16))
"""
FIRST OUTPUT 
5AD
SECOND OUTPUT
91 
THAT IS 
9*16^1+1*16^0=144+1=145
"""
