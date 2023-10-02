from timeit import Timer
pop_zero=Timer("x.pop(0)","from __main__ import x")
pop_end=Timer("x.pop()","from __main__ import x")
x=list(range(2000000))
print(f"pop(0): {pop_zero.timeit(number=1000):10.5} milliseconds")
x=list(range(2000000))
print(f"pop();{pop_end.timeit(number=1000):10.5f} milliseconds")

pop_zero=Timer("x.pop(0)","from __main__ import x")
pop_zero=Timer("x.pop()","from __main__ import x")
print(f"{'n':10s}{'pop(0)':>15s}{'pop()':>15s}")
for i in range(1_000_000,100_000_001,1_000_000):
    x=list(range(i))
    pop_zero_t=pop_zero.timeit(number=1000)
    x=list(range(i))
    pop_end_t=pop_end.timeit(number=1000)
    x=list(range(i))
    pop_end_t=pop_end.timeit(number=1000)
    print(f"{i:<10d}{pop_zero_t:>15.5f}{pop_end_t:15.5f}")
    

"""
pop(0):      2.377 milliseconds
pop();   0.00003 milliseconds
n                  pop(0)          pop()
1000000           0.00003        0.00002
2000000           0.00003        0.00002
3000000           0.00002        0.00003
4000000           0.00003        0.00005
5000000           0.00003        0.00002
6000000           0.00003        0.00003
7000000           0.00002        0.00003
8000000           0.00003        0.00003
9000000           0.00008        0.00002
10000000          0.00003        0.00003
11000000          0.00003        0.00003
12000000          0.00003        0.00003
13000000          0.00002        0.00002
14000000          0.00003        0.00003
15000000          0.00002        0.00003
16000000          0.00002        0.00002
17000000          0.00002        0.00003
18000000          0.00003        0.00003
19000000          0.00003        0.00002
20000000          0.00003        0.00004
21000000          0.00003        0.00002
22000000          0.00003        0.00003
23000000          0.00003        0.00003
24000000          0.00003        0.00002
25000000          0.00003        0.00002
26000000          0.00003        0.00002
27000000          0.00003        0.00002
"""
