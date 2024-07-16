import math

'''1.9 String Formatting'''
# never knew about sep, nor the dictionary formatting. Nice
print("Yes", "hello", "is", "anyone", "there", sep="...")
yep = {"age":23, "money":420.69}
print("He is %(age)d years old and has %(money).2f dollars." % yep)
# interesting, a little unusable, but still...
print(f"Age:{yep['age']:.>7}\n" + f"Money:{'$':.>4}{yep['money']:5.2f}")

'''1.10 Control Structures'''
# List comprehension. Really try to start using this in your code. Cleans things up a lot. But make sure it's readable.
# sq_list = [x ** 2 for x in range(6) if x % 2 != 0]
# print(sq_list)

'''1.11 Exception Handling'''
# Two types of errors in programs. We have syntax errors, which are caught by the compiler,
# and we have runtime errors, which we call Exceptions. We an exception occurs, we say that an exception has been raised.
# We can handle an exception that gets raised by using a try-except statement.
# Try-except will NOT cause the program to exit, and will continue executing the statements following that block.
# try:
#     math.sqrt(-1)
# except ValueError as err:
#     print("Mate:", err)
#     print(math.sqrt(abs(-1)))
# print("Continuing on...")

'''1.12 Defining Functions'''
# infinite monkey theorem. Goal: "afternoon punters and dribblers". 31 chars.
# letters = 'abcdefghijklm nopqrstuvwxyz'
# goal_str = 'afternoon punters and dribblers'
# score = 0
# monkey_str = '-------------------------------'
# ctr = 0
# while score != 31:
#     rand_i = random.randint(0,30)
#     if monkey_str[rand_i] != goal_str[rand_i]:
#         monkey_str = monkey_str[:rand_i] + letters[random.randint(0,26)] + monkey_str[rand_i+1:]
#         if monkey_str[rand_i] == goal_str[rand_i]:
#             score += 1
    
#     ctr += 1
#     if ctr % 100 == 0:
#         print(score, monkey_str)

# print(ctr, score, monkey_str)

'''1.13 Defining Classes'''
'''A couple things to learn here. For functions more generally, we've learnt that parameters are not inherently typed in Python.
We say they are 'duck typed', which means that we don't inherently define variables/parameters, we just examine they behaviour.
If it looks and quacks like a duck, then it is a duck. The advantage of this is that the compiler can be more lightweight since 
it doesn't have to do as much type checking. There are also type hints now too: '''
# def add(num1: float, num2: float) -> float:
#     return num1 + num2
# print(add(1.2, 2))
''' You should aim to always use type hints. They are NOT enforced, but may cause errors with other libraries. Any time you have
a complex parameter type, just set it to Any. Type hints essentially act as good documentation for when you come back to your code. 
Use them always. We can also define the return type of a function with the arrow -> shorthand. Return typing also isn't enforced 
by the compiler and is again used for documentation rather than compilation.
The reason you weren't up to date with this is because it was only introduced in Python 3.5.
'''

class Fraction:

    def __init__(self, num: int, den: int):
        if type(num) == float and num % 1 == 0:
            num = int(num)

        if type(den) == float and den % 1 == 0:
            den = int(den)

        if not (type(num) == int and type(den) == int):
            raise ValueError("Fraction inputs must be integer.")
        
        if den == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        
        if den < 0:
            den = -den
            num = -num
        
        gcd = math.gcd(num, den)
        while gcd > 1:
            num = num / gcd
            den = den / gcd
            gcd = math.gcd(int(num), int(den))
        self.num = num
        self.den = den

    # Pretty important here. Whenever you make a custom class, you should by second nature create the __repr__ function.
    # So create __init__ and __repr__ always, then use encapsulation (getters and setters) too. Repr is so important because
    # it provides a way to debug your class when it creates an error. Essentially, if __str__ is not defined it actually defaults
    # to __repr__. The way to think about it is: the goal of __repr__ is to be unambiguous for developers, and the goal of
    # __str__ is to be readable for users.

    def __repr__(self):
        return "Fraction(%d, %d)" % (self.num, self.den)

    def __str__(self):
        # Note how %d casts to an int
        return "%d/%d" % (self.num, self.den)
    
    def __add__(self, fraction2):
        num = self.num * fraction2.den + fraction2.num * self.den
        den = self.den * fraction2.den
        return Fraction(num, den)
    
    # Real interesting here. This refers to Right-hand addition. I.e. how should the compiler deal with 3 + Fraction(2,3) ?
    # It defaults to 3's __add__ function, but that function doesn't specify how to work with your new Fraction class.
    # If that returns NotImplemented, then the Fraction's radd method is checked. Nice. You have this for all arithmetic operations.
    # Then you also have __iadd__, which is iterative addition, i.e. 3 += Fraction(1, 2).
    def __radd__(self, other):
        if not type(other) == int:
            raise ValueError("Can only add Fraction to integer.")

        num = self.num + other * self.den
        return Fraction(num, self.den)

    def __mul__(self, fraction2):
        num = self.num * fraction2.num
        den = self.den * fraction2.den
        return Fraction(num, den)
    
    # Test deep vs shallow equality by commenting these two lines out. When they're commented, even though the equality check a couple lines down
    # tests two identical objects, the equality check returns False. More on shallow vs deep a bit lower.
    def __eq__(self, fraction2):
        return self.num == fraction2.num and self.den == fraction2.den
    
    def __gt__(self, fraction2):
        return (self.num / self.den) > (fraction2.num / fraction2.den)
    
    def __ge__(self, fraction2):
        if not self.__eq__(fraction2):
            return self.__gt__(fraction2)
        return True
    
    def __lt__(self, fraction2):
        return (self.num / self.den) < (fraction2.num / fraction2.den)
    
    def __le__(self, fraction2):
        return fraction2.__ge__(self)
    
    def get_num(self):
        return self.num
    
    def get_den(self):
        return self.den

fraction1 = Fraction(6,9)
print(fraction1)
fraction2 = Fraction(1,6)
print(fraction1 + fraction2)
print(fraction1 * fraction2)
print(fraction1 == Fraction(6,9))
print(fraction1 > Fraction(6,9))
print(fraction1 >= Fraction(7,9))
print(fraction1 < Fraction(7,9))
print(fraction1 <= Fraction(5,9))
print(3 + fraction1)

'''
Since I've just used it above, let's learn string formatting. The different kinds are as follows:
%r - raw data, %d - integer, %f - float, %s - string, %x - hexadecimal %o - octal.
Using these actually typecasts the variable before printing.
%r is useful if you want to avoid errors and just understand what's going on. It's actually the same
as just printing the object directly, %r just allows you to interpolate it into a string.
With a class you can actually define how it's formatted as a string in %s with def __str__(self)
'''
var = 69
print("Raw: %r, int: %d, float: %.2f, str: %s, hex: %x, oct: %o" % (var, var, var, var, var, var))
print("Raw: %r, str: %s" % (fraction1, fraction1))

'''
Really good stuff above on classes. In particular the fact that you can redefine all the builtin methods
for any class that you create. Now, more on the equality operator (==) in Python.
'''
ls = []
ls.append(1)
if ls == [1]:
    print("Bingo")
if ls is [1]:
    print("Bingo Too")
'''
As you can see, the equality operator is a shallow equality test. The identity operator (is) instead checks
that the objects have the same memory address. Note here: Python uses the same address for small integers, strings, etc.
Look at following:
'''
a = 'something'
b = 'something'
id(a)
# 139702804094704
id(b)
# 139702804094704
a is b
# True
'''But if you change it a bit:'''
a = 'something else'
b = 'something else'
id(a)
# 139702804150640
id(b)
# 139702804159152
a is b
# False
'''
We're getting False because the memory locations have been changed.

Relating this back to classes, if you create a custom class as above and don't define __eq__, whenever you use
an equality operator between instances of your custom class it will actually default to the identity operator (is).
So for example my_fraction == Fraction(2, 3) always equals False unless __eq__ is defined.
A simple way to define it as according to stack overflow:
'''

class Foo:
    def __init__(self, item):
        self.item = item

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    # Note that defining ne is no longer necessary in Python 3.
    # def __ne__(self, other):
    #     return not self.__eq__(other)

'''
Last thing to note with classes. A custom class constructor should always invoke the constructor
of its parent before continuing on with its own data and behaviour.'''

'''1.15 Key Terms'''

'''Abstract Data Type (ADT): essentially where behaviour is defined but not implementation. 
Examples include List, Queue, Set, Tree, etc.
Note that an ADT is not necessarily the opposite of a Primitive data type; arrays are examples of
non-primitive, non-abstract data types.

Primitive data type: a basic data type from which all other data types are constructed. Examples include
int, string, float, etc.

Encapsulation: this refers to the idea of only allowing the modification of a Class's variables by methods within that class.
I.e. encapsulate both the assignment and modification of variables WITHIN a class.
Practically this refers to using getter and setter functions in a custom class. Encapsulation is a good programming principle.

String interpolation: allows for the use of template variables directly within a string.'''

# Great idea to learn interfaces and structs in the future too.
# Make sure you really understand the difference between an interface, a struct and a class.