#Devisa an experiment to verify that the list  index operator is O(1)
from timeit import Timer
import random

def test1():
    x=[10,20,30,40,50]
    k=x[1]
def test2():
    x=[10,20,30,40,50]
    k=x[4]

def test3():
    another_x=[10,20,30,40,50,90,100,200,388]
    k=another_x[1]

t1=Timer("test1()","from __main__ import test1")
print(f"first test:{t1.timeit(number=1000):15.10f} milliseconds")

t2=Timer("test2()","from __main__ import test2")
print(f"second test:{t2.timeit(number=1000):15.10f} milliseconds")

t3=Timer("test3()","from __main__ import test3")
print(f"third test:{t3.timeit(number=1000):15.10f} millseconds")

"""
The change in time can be because of the process as you can see but the t1 and t2 is O(1)
ctice/day1.py
first test:   0.0000741730 milliseconds
second test:   0.0001598700 milliseconds
third test:   0.0001210370 millseconds
~/Documents/PythonPractice$ /bin/python3 /home/Documents/PythonPractice/day1.py
first test:   0.0000743130 milliseconds
second test:   0.0000729160 milliseconds
third test:   0.0000769670 millseconds

"""
#more will be added here today
