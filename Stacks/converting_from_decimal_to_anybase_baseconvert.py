#Converting decimal to binary(divby2) 
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

def divide_by_2(decimal_num):
  rem_stack=Stack()

  while decimal_num>0:
    rem=decimal_num%2
    rem_stack.push(rem)
    decimal_num=decimal_num//2

  bin_string=""
  while not rem_stack.is_empty():
    bin_string=bin_string+str(rem_stack.pop())
  return bin_string

print(divide_by_2(42))
print(divide_by_2(31))

"""
Output
11001
19
 """"""""""
"""
