import math
import cProfile
import time
from timeit import Timer

'''2.2 Algorithm Analysis
There's a big difference between a program and the algorithm the program is representing. One algorithm can be implemented 
in many different ways/programs. So, we should analyse the different ways to find the most efficient implementation.
Checking the running time of a function can be very useful, especially if it's called multiple times in the running of company systems.
'''

def multiply(a, b):
    start = time.time()
    for i in range(100000):
        a = a+i
    end = time.time()
    return end-start, a*b
cProfile.run('multiply(54,123)')

seconds, result = multiply(2, 3)
print(f"Took {seconds} seconds and result was {result}")


'''
An algorithmic case: build an anagram checker between two words.
The immediate idea is to sort both anagrams and see if they're equal. Fast, but not the most optimal. O(n log n) but O(n) is possible.
How you wonder?
Frequency counts. You only need to run through each anagram once, then just check the frequency counts.
The reason why you can use frequency counts here to save efficiency is because ORDER DOESN'T MATTER.
So, when order doesn't matter in your problem, use frequency counts.
'''

'''2.6 Lists
Just look at the examples below. Really great stuff.
'''
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
print(f"concatenation: {t1.timeit(number=1000):15.2f} milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print(f"appending: {t2.timeit(number=1000):19.2f} milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print(f"list comprehension: {t3.timeit(number=1000):10.2f} milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print(f"list range: {t4.timeit(number=1000):18.2f} milliseconds")

# concatenation:            0.96 milliseconds
# appending:                0.03 milliseconds
# list comprehension:       0.02 milliseconds
# list range:               0.01 milliseconds
'''
Pretty insane. The List range is much, much faster. List comprehension is always good too.

Looking at List operations in Python:

index assignment: O(1)
append: O(1)
pop(): O(1)

From there it's all O(n):

pop(i): O(n)
insert(i, item): O(n)
del operator: O(n)
iteration: O(n)
contains (in): O(n)
sort: O(n log n)

Basically, think of lists as a continuous block of memory stored at an address. If you wanna
change the structure of the list, i.e. insert or delete into the middle of it, you have to move
the rest of the list down/up. That includes inserting/deleting the first value - the whole new list
has to be moved up. Inserting/deleting towards the end of a list is less resource-heavy.

Other thing to note is that lists are pretty much Python's version of arrays, but not exactly. Python's
lists are so effective because they are very flexible and can hold completely different types of data.
However, because of this they use a fair bit of space.

The default array library offers a less space-intensive solution through array.array, but this can only
hold the same data type at each index. 

As for when to use what: use ordinary lists 90% of the time, use numpy arrays when working with numbers,
and use array.array when you really need to reduce space complexity with a homogeneous array.
'''
# Note that:
a = [1, 2, 3]
a[1] = 5
print(a)
# Reassigning an element in the middle of a list in Python is O(1). I actually think this is regardless of what you reassign it to.
# E.g. you could reassign a[1] = "New string" and it'd still be O(1). Yeah. Because Python lists are actually just lists of pointers.
# So assigning a[1] actually just puts a new pointer into the memory address at a[1], which points to the address of the string.

'''2.7 Dictionaries

get key/value: O(1)
set key/value: O(1)
del key/value: O(1)
contains: O(1)

These are ON AVERAGE. There are rare cases where these degenerate to O(n) performance.

'''