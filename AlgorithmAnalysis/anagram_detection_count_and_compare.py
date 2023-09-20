"""non commented code"""
"""COMMENTED CODE IS AT THE BOTTOM"""
def anagram_solution_4(s1,s2):
    c1=[0]*26
    c2=[0]*26
    
    for i in range(len(s1)):
        pos=ord(s1[i])-ord("a")
        c1[pos]=c1[pos]+1
    
    for i in range(len(s2)):
        pos=ord(s2[i])-ord("a")
        c2[pos]=c2[pos]+1
        
    j=0
    still_ok=True
    while j<26 and still_ok:
        if c1[j] == c2[j]:
            j=j+1
        else:
            still_ok=False
    return still_ok
    
print(anagram_solution_4("apple","pleap"))
print(anagram_solution_4("abcd","dcba"))
print(anagram_solution_4("abcd","dcda"))







"""Commented program """
"""
THINGS TO REMEMBER BEFORE LOOKING AT THIS PROGRAM
ord() function gives you the unicode 
for exmple print(ord("a")) //output: 97

Two lists c1 and c2 are initialized with 26 zeros each 
These lists will store the frequency of each letter of the alphabet for strings s1 and s2 respectively
that is counter initialization,
                  C1=[0]*26
                  C2=[0]*26
                  
"""
"""The more explaination of the code is available just below of the program """
def anagram_solution_4(s1,s2):
    c1=[0]*26
    c2=[0]*26

    """The work of this iteration is that to find each element position and increment it in the first string"""
    for i in range(len(s1)):
        pos=ord(s1[i])-ord("a")
        c1[pos]=c1[pos]+1
    """The work of this iteration is that to find each element position and increment it in the second string"""  
    for i in range(len(s2)):
        pos=ord(s2[i])-ord("a")
        c2[pos]=c2[pos]+1
    """Here it will check each character list that is of c1 and c2 , just to know that if they are equal
      here the iteration is going on
    """    
    j=0
    still_ok=True
    while j<26 and still_ok:
        if c1[j] == c2[j]:
            j=j+1
        else:
            still_ok=False
    return still_ok
    
print(anagram_solution_4("apple","pleap"))
print(anagram_solution_4("abcd","dcba"))
print(anagram_solution_4("abcd","dcda"))
"""------------------------------------TIME COMPLEXITY BIG O RUNNING TIME -----------------------------------------------------""""
"""
O(n)
linear time but could do so, by taking additional storage to keep the two lists of characters count
This algorithm sacrificed space in order to gain time 

i=n
while i>0:
  l=2+2
  i=i

  Time complexitiy O(logn)
  The value of i is cut in half each time through the loop so it will only take log n iterations
"""
