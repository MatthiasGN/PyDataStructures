import math
import cProfile
import time

'''2.2 Algorithm Analysis'''
'''
There's a big difference between a program and the algorithm the program is representing. One algorithm can be implemented 
in many different ways/programs. So, we should analyse the different ways to find the most efficient implementation.
'''

def multiply(a, b):
    for i in range(10000):
        a = a+i
    return a*b
cProfile.run('multiply(54,123)')