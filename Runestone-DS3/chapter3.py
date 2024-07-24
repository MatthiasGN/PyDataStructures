

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

'''

'''3.3 Stacks

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