# hashing a string called cat 
"""
HASHING STRING USING ORDINAL VALUE
IF I USE TAC WHICH IS ANAGRRAM OF CAT 
HERE WE CAN SEE THE COLLISION
"""
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum%tablesize

print(hash("cat", 11))
print(hash("tac", 11))
#output
# 4

"""
HASHING STRING USING ORDINAL VALUE WITH WEIGHTHING
WE USE THIS TECHNIQUE TO AVOID COLLISION
"""
def hash(astring, tablesize):
    sum = 0
    check = 0
    for pos in range(len(astring)):
            check = pos + check
            sum = sum + ord(astring[pos]) * check
    
    return sum % tablesize

print(hash("cat",11))
print(hash("tac",11))


# output
# 5
# 9 
#
