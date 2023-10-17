#This program is checking if the String have balanced parentheses or not
# Means to say that if it have a opening parentheses it should also have closing parentheses.
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

def par_checker(symbol_string):
    s=Stack()
    for symbol in symbol_string:
        if symbol=="(":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()
    return s.is_empty()
print(par_checker("((()))"))
print(par_checker("((()()))"))
print(par_checker("(()"))
print(par_checker(")("))
#This section will be updated today
