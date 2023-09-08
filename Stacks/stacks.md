





# Stack in python

Here I am going to write about stacks in python 

For this think of a tower of plate 
A data structure in which all insertions and deletion are made at one end and, and called the top of the stack.

Last in First Out





## Some Methods

- append(item): add item to top of stack
- push(item): push item to the top of the stack
- pop(item): remove and return the top item 
- peek(item): return the top item without removing item
- is_empty(item): return true if the stack is is_empty

## More

Stack inserttion and deletion happpen at the same time 

## Application

- reverse polish notation for evaluating arithmetic expressions
- Syntax parsing
- Cold Stack
- Used in recursion
- Undo and redo operations in word processors
- Low level assembly programming 

## Simple program 

```python
class Stack:
  def __init__(self):
    self.items=[]
  def is_empty(self):
    return not self.items
  def push(self,item):
    self.items.append(item)
  def pop(self):
    return self.items.pop()
  def peek(self):
    return self.items[-1]
  def size(self):
    return len(self.items)
  def __str__(self):
    return str(self.items)

if __name__=="__main__":
  s=Stack()
  print(s)
  print(s.is_empty())
  s.push(3)
  s.push(7)
  s.push(5)
  print(s)
  print(s.pop())
  print(s)
  print(s.peek())
  print(s.size())
```



## Reverse the order

Characters that are pushed first are popped last or
Characters that are pushed last are popped first(LIFO)
```python
class Stack:
  def __init__(self):
    self.items=[]
  def is_empty(self):
    return not self.items
  def push(self,item):
    self.items.append(item)
  def pop(self):
    return self.items.pop()
  def peek(self):
    return self.items[-1]
  def size(self):
    return len(self.items)
  def __str__(self):
    return str(self.items)

if __name__=="__main__":
  s=Stack()
  string="nIekniL htiw tol a nraeL"
  reversed_string=""
  for char in string:
    s.push(char)   #character that are pushed last
  while not s.is_empty():
    reversed_string +=s.pop()  #are popped first
  print(reversed_string)

#output Learn a lot with LinkedIn
kjl

