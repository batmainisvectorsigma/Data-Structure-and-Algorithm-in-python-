#scroll down to know more about the program
import timeit
import random

print(f"{'n':10s}{'list':10s}{'dict':10s}")
for i in range(10_1000,1_000_001,20_000):
    t=timeit.Timer(f"random.randrange({i}) in x", "from __main__ import random, x")
    x=list(range(i))
    lst_time=t.timeit(number=1000)
    x={j: None for j in range(i)}
    dict_time=t.timeit(number=1000)
    print(f"{i<10,}{lst_time:>10.3f}{dict_time:>10.3f}")
    
"""
n         list      dict      
(False,)     0.248     0.001
(False,)     0.283     0.001
(False,)     0.351     0.001
(False,)     0.484     0.001
(False,)     0.537     0.001
(False,)     0.560     0.001
(False,)     0.561     0.001
(False,)     0.629     0.001
(False,)     0.701     0.001
(False,)     0.749     0.001
(False,)     0.815     0.001
(False,)     0.939     0.001
(False,)     0.916     0.001
(False,)     0.991     0.001
(False,)     1.016     0.001
"""
#-------------------------------------------------------------------------ABOUT THE PROGRAM----------------------------------------------------------------------------------------------------
"""
create a list of nummbers
pick a number
check whether it is in the list or not
check the time to check the num
increase the list size 
check the time to check the num
first x is list 
and second x is of dictionary


"""
