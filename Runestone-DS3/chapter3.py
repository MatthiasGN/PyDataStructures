from typing import Any
import random

'''3 Data Types
When we give an abstract data type (ADT) a physical implementation, we can now refer to that implementation as a data structure.

What different types of data structures exist in Python?

Primitive:
- Characters
- Integers
- Floats
- Booleans

Non-Primitive (built-ins):
- Lists
- Dictionaries
- Sets
- Tuples

Non-Primitive (user-defined):
- Stacks
- Queues
- Deques
- LinkedLists
- Trees
- etc


3.3 Stacks

Our first linear data type. Addition and removal of new items is at the same end; the top of the stack.
We call this last in, first out (LIFO). The thing to remember with FIFO and LIFO is that the first part
of the anagram refers to when the item that is being removed was added to the data structure. While the second
part of the anagram refers to the position of the item being removed. So FIFO would mean the first item to be
added to the data structure is removed from the first position.

Stacks are pretty easy to think about: just consider a stack of books.

A useful idea to consider is that stacks essentially reverse the order of insertion to the order of removal.
I.e. if you looped through a list and added each item into a stack, the stack automatically has reversed the order
of that list.

A good example is the idea of your current tab history. Your current webpage is on the top of the stack, but you
can hit back as many times as you want to move in reverse order through the webpages.

Stacks are ordered LIFO.

The really important thing here is to note how it's implemented in Python. The element at the bottom of the stack is
actually the first element in the Python List. This makes it much more efficient to push and pop items from the top of
the stack (i.e. the end of the list, which is less memory intensive).
'''

class Stack:

    def __init__(self):
        self.ls = []

    def __repr__(self):
        return f"Stack({self.ls})"

    def push(self, obj: any):
        self.ls.append(obj)

    def pop(self):
        return self.ls.pop()

    def is_empty(self):
        return len(self.ls) < 1

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.ls[-1]
    
    def size(self):
        return len(self.ls)
    
# Four principles of OOP:
# Encapsulation - both data and methods are contained within the same object. I.e. getters and setters
# Inheritance - classes can inherit variables and methods from parent classes
# Polymorphism - classes can be treated as instances of their parent classes. E.g. Dog can be input to a function that only accepts Animal
# Abstraction - complex ideas can be represented in a number of different, simpler ways. E.g. a stack, an ADT, can be implemented in Python as a data structure in multiple ways.

s = Stack()
s.push(1)
s.peek()
print(s)
print(s.pop())
s.push(1)
s.push(2)
s.push(3)
print(s)


'''3.6 Balanced Parentheses
Balancing parentheses is almost always achieved through Stacks.
'''

def par_checker(pars):
    s = Stack()
    for par in pars:
        if par in '({[':
            s.push(par)
        elif not s.is_empty():
            if abs(ord(par)-ord(s.peek())) < 3:
                s.pop()
            else:
                return False
        else:
            return False
        
    return s.is_empty()

print(par_checker("((()))"), end=", ")  # expected True
print(par_checker("((()()))"), end=", ")  # expected True
print(par_checker("(()"), end=", ")  # expected False
print(par_checker(")("), end=", ")  # expected False
print(par_checker('{({([][])}())}'), end=", ")
print(par_checker('[{()]'))

'''A really interesting way to check for equality between two alphabet-like structures. Use index to match by position!'''
def matches(sym_left, sym_right):
    all_lefts = "([{"
    all_rights = ")]}"
    return all_lefts.index(sym_left) == all_rights.index(sym_right)


'''3.8 Decimal to Binary
Something you may be noticing is that Stacks are a great choice of data structure whenever a REVERSAL of order is required in the algorithm.
'''

def base_converter(num: int, base: int) -> str:
    digits = '0123456789ABCDEF'

    s = Stack()
    while num > 0:
        s.push(num % base)
        num = num // base
    
    binary = ''
    while not s.is_empty():
        binary += digits[s.pop()]
    return binary

print(base_converter(233, 2), end=", ")
print(base_converter(233, 3), end=", ")
print(base_converter(233, 8), end=", ")
print(base_converter(233, 16))


def infix_to_postfix(infix: str) -> str:
    op_stack = Stack()
    operators = '+-/·^()'
    tokens = infix.split()
    postfix = ''

    for token in tokens:
        if token in operators:
            if token == ')':
                postfix += op_stack.pop()
            elif token != '(':
                op_stack.push(token)
        else:
            postfix += token
    
    return postfix

print(infix_to_postfix('( ( A + B ) · C )'), end=", ")
print(infix_to_postfix('( ( A · B ) + ( C · D ) )'), end=", ")
print(infix_to_postfix('( ( ( A + B ) · C ) - ( ( D - E ) · ( F + G ) ) )'), end=", ")
print(infix_to_postfix('( 5 · ( 3 ^ ( 4 - 2 ) ) )'))

def postfix_eval(postfix: str) -> int:
    tokens = postfix.split()
    operands = Stack()
    operators = '+-/·'

    for token in tokens:
        if token not in operators:
            operands.push(int(token))
        else:
            # if there are two operands, 
            num1, num2 = operands.pop(), operands.pop()
            if token == '+':
                operands.push(num2 + num1)
            elif token == '-':
                operands.push(num2 - num1)
            elif token == '/':
                operands.push(num2 / num1)
            elif token == '·':
                operands.push(num2 * num1)
    
    return operands.pop()

print(postfix_eval("7 8 + 3 2 + /"))

'''3.10 Queues
A queue adds to the front and deletes from the end. We call these operations enqueue and dequeue. A queue is FIFO, 
so the first element added (in history) is the first one out. We only have a pointer to the front and the back, 
making mid-queue operations expensive.
'''

class Queue:

    def __init__(self) -> None:
        self.items = []

    def __repr__(self) -> str:
        return f"Queue({self.items})"
    
    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return self.size() == 0

    def enqueue(self, item) -> None:
        self.items.insert(0, item) # O(n) !

    def dequeue(self) -> Any:
        return self.items.pop() # O(1). You can swap these by defining the front and rear the opposite way.


def josephus(names: list, num: int) -> str:
    names_left = Queue()
    for name in names:
        names_left.enqueue(name)

    while names_left.size() > 1:
        for i in range(num):
            names_left.enqueue(names_left.dequeue())
        names_left.dequeue()
    
    return names_left.dequeue()
        
print(josephus(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))


'''3.15 Deques

Double-ended queue. Can add and remove from both the front and the rear. Essentially combines the capabilities 
of the stack and queue. Deques actually don't require either of FIFO or LIFO - it's up to the developer to stay
consistent and keep track of which end is the front.
'''

# Actually super useful for shortening data structure class logic
print("\n~~~Deques~~~\n")
print(bool([]))
print(bool([1]))


class Deque:

    def __init__(self) -> None:
        self.items = []

    def __repr__(self) -> str:
        return f"Deque({self.items})"
    
    def is_empty(self) -> bool:
        return not bool(self.items)
    
    def add_front(self, item) -> None:
        self.items.append(item)

    def remove_front(self) -> Any:
        return self.items.pop() 
    
    def add_rear(self, item) -> None:
        self.items.insert(0, item) # O(n)

    def remove_rear(self) -> Any:
        return self.items.pop(0) # O(n)

    def size(self) -> int:
        return len(self.items)


def palindrome_checker(pal: str) -> bool:
    pal_deq = Deque()
    for char in pal:
        pal_deq.add_front(char)

    while not pal_deq.is_empty():
        if pal_deq.size() == 1:
            return True
        if pal_deq.remove_front() != pal_deq.remove_rear():
            return False

print("Palindromes: ", end="")
print(palindrome_checker("racecar"), end=", ")
print(palindrome_checker("lsdkjfskf"), end=", ")
print(palindrome_checker("radar"))


'''3.19 Lists

We start with a singly LinkedList. Recall that each item in the list is a Node with a value and the address of the next Node.
We only have a head when referring to it - this makes appending items at the rear very expensive, but inserting at the head is very fast.


~~~~ Getters & Setters ~~~~

On a side note - doing some learning about getter and setter methods. Firstly, we refer to getter methods as accessors and 
setter methods as mutators. Now, what's the point of even having these at all? Why not just change the object values directly using dot notation?

Ok so the net is actually a bit divided on it. But it comes from Java, where if you didn't set up accessors and mutators when you first created
a class, but eventually needed to, your entire codebase using that class would be broken/need to be updated. It's also used to keep your class
implementation private - you can retrieve the values however you want to, which might require entering into a database or sending HTTP requests.

In general, it's good practice to use getters and setters but it's actually not fully required for Python, because PRIVATE INSTANCE VARIABLES DO NOT
EXIST IN PYTHON.

However, there is a great Pythonic implementation of it using the PROPERTY decorator. 
'''

class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"
    
    def get_value(self) -> Any:
        return self.value

    def set_value(self, value) -> None:
        self.value = value

    value = property(get_value, set_value)
    # Syntax: property(getter, setter, deleter)

    def get_next_node(self) -> Any:
        return self.next

    def set_next_node(self, next) -> None:
        self.next = next

    next = property(get_next_node, set_next_node)
    

'''
In the case above, the property decorator isn't so important. But the reason it might be important is, say our set_value function was as follows:

def set_value(self, value) -> None:
    if value < 0:
        self.value = value
    elif value > 1000:
        self.value = 1000
    else:
        self.value = value

By setting the property with this more complex setter, we can now use that entire function by immediately calling Node.value = -69 in our code,
which would automatically use the property decorator to redirect to the set_value function, effectively setting Node.value = 0.
As you can see, it's especially important to use the property decorator when your accessors and mutators are more complex.
'''
    

node = Node(5)
print(node.value)
node.value += 1
print(node.value)

class UnorderedList:

    def __init__(self, head: Node) -> None:
        self.head = head

    def __repr__(self) -> str:
        return f"UnorderedList({self.head}, {self.head.value})"

    def add(self, item: Node) -> None:
        item.next = self.head
        self.head = item

    def remove(self, value: Node) -> None:
        if self.head.value == value:
            self.head = self.head.next
            return
        
        curr = self.head
        while curr.next is not None:
            if curr.next.value == value:
                curr.next = curr.next.next
                return
            curr = curr.next
        raise Exception("Item cannot be removed; does not exist in List.")        

    def append(self, item: Node) -> None:
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = item
    
