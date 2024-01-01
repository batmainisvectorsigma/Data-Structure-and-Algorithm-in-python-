# Converting an Integer to a String in any base Using a Stack
class Stack:
    def __init__(self):
        self._items=[]
    def is_empty(self):
        return not bool(self._items)
    def push(self,item):
        self._items.append(item)
    def pop(self):
        return self._items.pop()
    def peek(self):
        return self._items[-1]
    def size(self):
        return len(self._items)

rStack = Stack()

def toStr(n,base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ""
    while not rStack.is_empty():
        res = res + str(rStack.pop())
    return res

print(toStr(1453,16))
"""
OUTPUT 
5AD
"""
