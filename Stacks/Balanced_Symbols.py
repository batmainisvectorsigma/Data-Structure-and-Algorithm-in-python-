#Problem
"""
balancing and nesting different kindcs of opening and closing symbols occurs frequently 
and we are checking if the symbols are balanced or not 
"""
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

def balance_checker(symbol_string):
    s=Stack()
    for symbol in symbol_string:
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                if not matches(s.pop(),symbol):
                    return False
    return s.is_empty()

def matches(sym_left,sym_right):
    all_lefts="([{"
    all_rights=")]}"
    return all_lefts.index(sym_left) == all_rights.index(sym_right)

print(balance_checker('{({([][])}())}'))    
print(balance_checker('[{()]'))
