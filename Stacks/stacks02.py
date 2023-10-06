#Read stacks.md to know more about about stacks 
# stacks.md file is in Stacks directory
#Write a program to reverse the order
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


#more updates will be available soon
