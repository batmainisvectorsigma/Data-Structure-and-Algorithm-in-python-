def BinaryTree(r):
    return [r, [], []]
    
def insertLeft(root,newBranch):
    t=root.pop(1) #removing item if there is item
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root
def insertRight(root,newBranch):
    t=root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]
    
def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]
    
r=BinaryTree(3)
print(insertLeft(r,4))
print(insertLeft(r,5))
print(insertRight(r,6))
print(insertRight(r,7))
l=getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))

"""
OUTPUT
[3, [4, [], []], []]
[3, [5, [4, [], []], []], []]
[3, [5, [4, [], []], []], [6, [], []]]
[3, [5, [4, [], []], []], [7, [], [6, [], []]]]
[5, [4, [], []], []]
[3, [9, [4, [], []], []], [7, [], [6, [], []]]]
[3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]
[6, [], []]
"""



"""
ABOUT THE PROGRAM
1st step 
insert in first item
2nd step
insert in first subchild
3rd step 
insert in second subchild




"""
