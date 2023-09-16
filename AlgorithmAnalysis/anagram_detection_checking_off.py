def anagram_solution(s1, s2):
    # If lengths of both strings are not same, they can't be anagrams.
    if len(s1) != len(s2):
        return False
    
    # Convert the second string to a list so that we can modify it.
    s2_list = list(s2)
    
    pos1 = 0
    still_ok = True
    
    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(s2_list) and not found:
            if s1[pos1] == s2_list[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            # If the character is found in s2_list, set its position to None.
            s2_list[pos2] = None
        else:
            still_ok = False

        pos1 += 1

    return still_ok

# Test the function
print(anagram_solution('heart', 'earth'))  # True
print(anagram_solution('python', 'typhon'))  # True
print(anagram_solution('apple', 'pale'))  # False
