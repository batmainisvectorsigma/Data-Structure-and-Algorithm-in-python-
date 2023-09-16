#without comment solution 
#scroll down to see the commented solution 
def anagram_solution_2(s1,s2):
    list1=list(s1)
    list2=list(s2)
    list1.sort()
    list2.sort()
    pos=0
    matches=True
    while pos<len(s1) and matches:
        if list1[pos] == list2[pos]:
            pos=pos+1
        else:
            matches=False
    return matches
    
print(anagram_solution_2("apple","pleap"))
print(anagram_solution_2("abcd","dcba"))
print(anagram_solution_2("abcd","dcda"))



#commented solution 
def anagram_solution_2(s1, s2):
    # Convert both strings to lists for easier sorting and comparison.
    a_list_1 = list(s1)
    a_list_2 = list(s2)

    # Sort both lists. If the strings are anagrams, their sorted lists should be identical.
    a_list_1.sort()
    a_list_2.sort()

    pos = 0           # Initialize position to start comparison from the first character.
    matches = True    # Assume the two sorted lists match until proven otherwise.

    # Loop through each position in the sorted lists and compare characters.
    while pos < len(s1) and matches:
        if a_list_1[pos] == a_list_2[pos]:
            # If the characters at the current position match, move to the next position.
            pos = pos + 1
        else:
            # If they don't match, set matches to False and exit the loop.
            matches = False

    # Return the final result.
    return matches

# Test the function.
print(anagram_solution_2("apple", "pleap"))  # Expected: True because when sorted both become "aelpp".
print(anagram_solution_2("abcd", "dcba"))    # Expected: True because when sorted both become "abcd".
print(anagram_solution_2("abcd", "dcda"))    # Expected: False because sorted s1 is "abcd" while sorted s2 is "acdd".
