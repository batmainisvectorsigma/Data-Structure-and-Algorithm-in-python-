class Stack:
  def __init__(self):
      self._items = []

  def is_empty(self):
      return not bool(self._items)

  def push(self, item):
      self._items.append(item)

  def pop(self):
      return self._items.pop()

  def peek(self):
      return self._items[-1]

  def size(self):
      return len(self._items)

def infixToPostfix(infixexpr):
  prec = {}
  prec["*"] = 3
  prec["/"] = 3
  prec["+"] = 2
  prec["-"] = 2
  prec["("] = 1
  opStack = Stack()
  postfixList = []
  tokenList = infixexpr.split()

  for token in tokenList:
      if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
          postfixList.append(token)
      elif token == '(':
          opStack.push(token)
      elif token == ')':
          topToken = opStack.pop()
          while topToken != '(':
              postfixList.append(topToken)
              topToken = opStack.pop()
      else:
          while (not opStack.is_empty()) and \
                (prec[opStack.peek()] >= prec[token]):
              postfixList.append(opStack.pop())
          opStack.push(token)

  while not opStack.is_empty():
      postfixList.append(opStack.pop())

  return " ".join(postfixList)

# Example usage
print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

#  output
#  A B * C D * +
#  A B + C * D E - F G + * -

