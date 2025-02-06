import random

"""
Recursion is a method of solving problems that involves breaking a problem down
into smaller and smaller subproblems until they are small enough to be solved trivially.

We start with an easy problem: calculating the sum of numbers in a list.
The simple way to implement that would be as follows:
"""

def list_sum(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum

print(list_sum([1,3,5,7,9]))

"""
How would we make this recursive?
Well, let's try to break down the problem.

list_sum([1,3,5,7,9]) is the same as 
1 + list_sum([3,5,7,9]).

Get the idea? If we generalise this, we end up with the following recurrence relation:

list_sum(num_list) = first(num_list) + list_sum(num_list - first(num_list))

Let's turn this into a recursive function.
"""

def list_sum_rec(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])
    
print(list_sum_rec([1,3,5,7,9]))

"""
And we get the same result. Two important things to note here;
first off, the first if check makes sure that the recursive function has an ESCAPE CLAUSE. A base case.
This means that at the smallest subproblem size, we stop recursion and return something directly.
The second thing to note is that a good way to think about recursion is to think backwards.
What's the simplest subproblem going to be, and does your function account for that base case?


With these ideas in mind, we come to:

4.4 The Three Laws of Recursion

1. A recursive algorithm must have a base case.
2. A recursive algorithm must change its state and move towards the base case.
3. A recursive algorithm must call itself (recursively).

Essentially, a key idea is that when the function calls itself, the parameters fed to it must change
in order to break the problem down into subproblems. Otherwise we end up with infinite recursion.

"""

def convert_base(int, base):
    convert_string = "0123456789ABCDEF"

    if int < base:
        return convert_string[int]
    else:
        remainder = int % base
        new_int = int // base
        return convert_base(new_int, base) + convert_string[remainder]
    
print(convert_base(769, 10))
print(convert_base(1453, 16))

"""
See how much simpler this solution is compared to using the divide by 2 algo with stacks?
"""

def reverse_str(str):
    if len(str) == 1:
        return str
    return str[-1] + reverse_str(str[:-1])

print(reverse_str("tester"))
    

"""
Simpler palindrome without stacks:
"""
from test import testEqual

def remove_white(s):
    new_s = ""
    for char in s:
        if char.isalpha():
            new_s += char
    return new_s

def is_pal(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_pal(s[1:-1])
    return False

testEqual(is_pal(remove_white("x")), True)
testEqual(is_pal(remove_white("radar")), True)
testEqual(is_pal(remove_white("hello")), False)
testEqual(is_pal(remove_white("")), True)
testEqual(is_pal(remove_white("hannah")), True)
testEqual(is_pal(remove_white("madam i'm adam")), True)