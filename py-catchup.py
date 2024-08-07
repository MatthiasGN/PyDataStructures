import sys
import os
import string
import random
import math
import numpy as np
import datetime
import calendar
import struct
import platform
import site
import subprocess
import multiprocessing
import cProfile
import socket
import time
import traceback
import glob
import json

# All exercises from w3resource.com.


# 1.
# print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

# 2.
# print(sys.version)

# 3.
# print(datetime.datetime.now())

# 4.
# r = input("r = ")
# print("Area = " + str(math.pi * float(r) ** 2))

# 5.
# name = input("First and last name please: ")
# print(name.split(" ")[1] + ", " + name.split(" ")[0])

# 6.
# data = input("Sample data: ")
# data_list = data.split(", ")
# data_tuple = tuple(data_list)
# print("List: ", data_list)
# print("Tuple: ", data_tuple)

# 7.
# file_name = input("Filename: ")
# print(file_name.split(".")[1])

# 8.
# ls = [1, 2, 3, 4]
# print("%s, %s" % (ls[0], ls[-1]))

# 9.
# exam_date = (11, 12, 2014)
# print("The exam is on %s" % datetime.date(exam_date[2], exam_date[1], exam_date[0]))

# 10.
# n = int(input("n: "))
# print("n + nn + nnn = %s" % (n + n * 11 + n * 111))

# 11.
# print(abs.__doc__)

# 12.
# print(calendar.month(2024, 10))

# 13.
# print("""Multi-line strings are back in the biz.
# Who knew, huh?
# Thought they were long gone.""")

# 14.
# date1 = datetime.date(2024, 10, 7)
# date2 = datetime.date(2024, 7, 5)
# print(date1-date2)

# 15.
# ~

# 16.
# ~

# 17.
# ~

# 18.
# ~

# 19.
# stringls = input("string: ")
# if len(stringls) > 1 and stringls[:2] == 'Is':
#     print(stringls)
# else:
#     print("Is" + stringls)

# 20.
# ~

# 21.
# ~

# 22.
# ~

# 23.
# ~

# 24.
# letter = input("Letter: ")
# if letter in 'aeiou':
#     print("Vowel")
# elif letter == 'y':
#     print("Uhhh")
# else:
#     print("Consonant")

# 25.
# ~

# 26.
# integers = [2,3,5,8,14,20,21,16,12,7,3,3,1]
# for num in integers:
#     ch = '~'*num
#     print(ch)

# 27.
# integers = [2,3,5,8,14,20,21,16,12,7,3,3,1]
# int_str = ""
# for num in integers:
#     int_str += str(num)
# print(int_str)

# 28.
# ~

# 29.
# ~

# 30.
# ~

# 31.
# ~

# 32.
# ~

# 33.
# ~

# 34.
# ~

# 35.
# ~

# 36.
# ~

# 37.
# ~

# 38.
# ~

# 39.
# ~

# 40.
# ~

# 41.
# file_name = input("filename: ")
# if os.path.isfile(file_name):
#     print("yep")
# else:
#     print("no")

# 42. To determine if a Python shell is executing in 32-bit mode or 64-bit mode on OS.
# The reason this works is because a struct is custom sized to the mode. I.e. 4 bits in 32-bit mode and 8 bits in 64-bit mode.
# print(struct.calcsize("P") * 8)

# 43.
# print(os.name)
# print(platform.system())
# print(platform.release())

# 44. Really good for understanding where the Python packages are. This is where all the pip files get installed.
# print(site.getsitepackages())

# 45.
# print(os.system('ls'))
# Below is better. More flexible
# print(subprocess.Popen("ls", shell=True).wait())

# 46.
# print("Current File Name: ", os.path.realpath(__file__))

# 47. Number of cores/CPUs being used. More CPUs allows for more multi-threading and running several applications at once.
# Especially important for video editing. Rendering. Useful for gaming with high graphics requirements too (also a form of rendering)
# print(multiprocessing.cpu_count())

# 48.
# ~

# 49.
# ~

# 50. Pretty nice line you never knew here. Could be really useful for constructing a string in a loop
# print("No newline", end="")
# print(", please")

# 51. Actually super useful for testing running times. cProfile. Use it.
# def multiply(a, b):
#     return a*b
# cProfile.run('multiply(54,123)')

# 52. Again, genuinely useful stuff here.
# print("*-------------------------*")
# print(os.environ)
# print("*-------------------------*")
# print(os.environ['HOME'])
# print("*-------------------------*")
# print(os.environ['PATH'])
# print("*-------------------------*")

# 53.
# ~

# 54. Socket stuff is really important for networking.
# local_host = socket.gethostname()
# ip_addresses = socket.gethostbyname_ex(local_host)[2]
# print(ip_addresses[0])

# 55.
# ~

# 56.
# ~

# 57. How you actually time something.
# def sum_of_n_numers(n):
#     start_time = time.time()
#     s = 0

#     for i in range(1, n+1):
#         s = s + i
    
#     end_time = time.time()

#     return s, end_time - start_time

# n = 5
# sol, tim = sum_of_n_numers(n)
# print("n = %s, solution is %s, time taken is %s" % (n, sol, tim))

# 58.
# ~

# 59.
# ~

# 60.
# ~

# 61.
# ~

# 62.
# ~

# 63.
# ~

# 64.
# ~

# 65.
# ~

# 66.
# ~

# 67.
# ~

# 68.
# ~

# 69.
# ~

# 70.
# ~

# 71.
# ~

# 72.
# ~

# 73.
# ~

# 74.
# ~

# 75.
# ~

# 76. One of the earliest things you learnt
# print(sys.argv)

# 77. Shows if your system is a big-endian or little-endian platform. Little endian means the digit of littlest significance is stored in memory first,
# big endian means the digit of biggest significance is stored in memory first.
# So e.g. 1011101 will have the right side stored first in little endian, and the left side first in big endian.
# Most platforms use little endian. However, protocols like TCP/IP are big endian.
# print(sys.byteorder)

# 78.
# print(sys.builtin_module_names)

# 79. Size in bytes of each variable. Note how the size is the same between strings / integers that arent too far apart. Thanks to padding.
# str1 = "four"
# str2 = "fives"
# int1 = 69
# int2 = 420

# print(str1 + ": " + str(sys.getsizeof(str1)))
# print(str2 + ": " + str(sys.getsizeof(str1)))
# print(str(int1) + ": " + str(sys.getsizeof(int1)))
# print(str(int2) + ": " + str(sys.getsizeof(int2)))

# 80. Really good manual attempt here. Need to learn exceptions properly
# def recursion_limit(n):
#     try:
#         return recursion_limit(n+1)
#     except Exception as err:
#         print(n, err)
# recursion_limit(1)
# print(sys.getrecursionlimit())

# 81.
# ~

# 82.
# ~

# 83.
# ~

# 84.
# ~

# 85.
# ~

# 86.
# ~

# 87.
# print(os.path.getsize("py-catchup.py"), "bytes")

# 88.
# ~

# 89.
# ~

# 90. open() opens a file and returns it as a file object. Default is 'r' read, also 'a' append, 'w' write, 'x' create.
# Actually a huge lesson here. I never use 'with'. I should use it more. Essentially allows for much more readable code
# as well as reusable exception handling. For example, look at the following:
# file = open('a.txt', 'w')
# try:
#     file.write('hello world')
# finally:
#     file.close()

# That whole thing can be condensed into:
# with open('a.txt', 'w') as file:
#     file.write('hello world')

# Error checking isn't even necessary because 'with' handles most cases. You can of course implement your own where necessary.
# Very useful for improving the quality and cleanliness of your code.
# 
# After a bit more research. Basically any time you're working with files or threading, you probably want to use a 'with' statement.
# It's a context manager, which means that it cleans up and manages multiple files, processes or threads working at the same time.
# Besides that it won't get much use. Is essentially a better version of try: finally:, though.

# src = 'py-catchup.py'
# dest = 'py-catchup-short.py'
# with open(src, 'r') as f, open(dest, 'w') as d:
#     for line in f:
#         d.write(line)

# 91.
# ~

# 92.
# ~

# 93. Interesting. id(object) gives you the memory address of the object.
# x = 53
# print("Identity: %s, Type: %s, Memory Address: %s" % (x, type(x), id(x)))

'''
94. Hijacking this question to learn about the different types of String literals available through prefixes.
First we have f-strings, e.g. f'Example'. An f-string is actually just a longer version of string.format.
name = "Matty"
adjective = "Genius"
print("{} is {}".format(name, adjective))
is the same as 
print(f"{name} is {adjective}")
Other languages have these features more naturally, so f-strings are Python's version.
For clarity, this process is called string interpolation - interpolating variables into strings.

Next we have b-strings. A byte string is literally a sequence of bytes, and isn't actually human-readable.
byte_str = b'Byte string'
print(byte_str)
So how come we can print this successfully? Well, Python decodes them from UTF-8 when you print them.
That's actually exactly what the 'print' function does - it converts byte information from memory to UTF-8 characters
for human readability.

Then we have r-strings. An r-string is a raw string. A good way to think about it is that an f-string
is essentially a string with batteries included, i.e. extra features. Whereas an r-string is a string with all
extra features removed, completely minimalist. An r-string ignores escape characters. So the use case for it
might be a function that feeds a string with escape characters into another function to eventually print it.

Finally we have u-strings. U-strings are unicode literals. Python3 strings are unicode by default so you
probably don't need to worry about these unless you venture into Python2 for work. U-strings allow you to use
non-ASCII characters (i.e. UTF-8) such as emojis, accented characters, etc.
'''

# 95.
# ~

# 96. Printing the call stack is done automatically with error checking. Could be useful.
# def f1():
#     return f2()

# def f2():
#     # n = 1/0
#     traceback.print_stack()

# f1()


# 97.
# ~

# 98. Note this one down. Useful for debugging, network information and random number seeds.
# print(time.ctime())

# 99. Underratedly useful.
# subprocess.Popen("clear", shell=True).wait()

# 100. 
# ~

# 101.
# ~

# 102. Pretty cool and probably useful tbh. You should be using subprocess more often.
# print(subprocess.check_output("ls", shell=True, universal_newlines=True))

# 103.
# ~

# 104.
# print(os.getegid())
# print(os.geteuid())
# print(os.getgid())
# print(os.getgroups())

# 105.
# print(os.environ)

# 106.
# ~

# 107.
# print(os.path.__file__)
# print(time.ctime(os.path.getmtime(os.path.__file__)))
# print(os.path.getsize(os.path.__file__))

# 108.
# ~

# 109.
# ~

# 110.
# ~

# 111. Actually pretty useful.
# print(glob.glob('*.py'))

# 112.
# ~

# 113.
# a = input("A: ")
# try:
#     a = int(a)
# except Exception as err:
#     print("Input must be a number.")
# print(a)

# 114.
# ~

# 115.
# ~

# 116.
# ~

# 117. Actually useful.
# a = 'aaa'
# b = 'aaa'
# print(hex(id(a)))
# print(hex(id(b)))

# 118.
# ~

# 119.
# ~

# 120.
# ~

# 121.
# ~

# 122.
# ~

# 123.
# print(sys.float_info)
# print(sys.int_info)
# print(sys.maxsize)

# 124.
# ~

# 125.
# ~

# 126.
# ~

# 127.
# ~

# 128.
# ~

# 129.
# ~

# 130.
# data = {'Alex': 1, 'Suresh': 2, 'Agnessa': 3}
# print(data)
# print(json.dumps(data))

# 131.
# ~

# 132.
# ~

# 133.
# ~

# 134. Genuinely a good function to learn. MAP.
# x, y = map(int, input("Input the value of x & y: ").split())
# print("The value of x & y are: ", x, y)

# 135.
# ~

# 136.
# ~

# 137.
# ~

# 138. Not bad either
# print(True.real)
# print(False.real)

# 139.
# ~

# 140.
# ~

# 141.
# num = 30
# print(str(hex(num)).split('x')[1])

# 142.
# ~

# 143.
# ~

# 144.
# ~

# 145.
# ~

# 146.
# ~

# 147.
# ~

# 148.
# ~

# 149.
# ~

# 150.
# ~