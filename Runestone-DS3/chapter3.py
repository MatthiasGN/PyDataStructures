from typing import Any
import random

'''3.2 Linear Data Structures

We'll start with lists, stacks, queues and deques.
A linear data structure is defined by how items are ordered according to how they are added or removed.
They also generally have a front and a rear (head and a tail).

Some structures may only allow addition to the tail, or some may only allow removal from the tail.

3.3 Stacks

Stacks are a linear data structure where addition and removal only happens at ONE end.
Typically this will be the tail, or the 'top'.

Think of it like a stack of books.
In Python, we implement the addition/removal end as the TAIL of a List.

E.g. stack = [1, 2, 3], 3 could be popped from the tail or an element could be pushed on top of it.
But accessing the element at the bottom of the stack, 1, is costly and difficult.

Stacks are last-in first-out, or LIFO. This means the item that was last added in is the first to be popped out.

One of the most fundamentally useful ideas behind a stack is the ordering. For example, you add books to a stack in some order.
Then if you pop those books one by one off the stack, the order you get is exactly the REVERSE of the order you added them in.
More formally, the order of insertion is the reverse of the order of removal.
This idea is fundamental to many uses of the Stack in DS&A.

To achieve this functionality with a list, you'd have to use two/multiple lists, i.e. extra space, and probably lose time efficiency.

A real-life example of this is your web page history within your current tab. You can hit the back button and forward button
to go back and forth down the stack. Another simple example is Ctrl+Z and Ctrl+Shift+Z for undo and redo.

Let's try to implement a Stack.
'''

class Stack:
    def __init__(self):
        self._items = []

    def __repr__(self):
        return f"Stack{self._items}"

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop() if self._items else None
    
    def peek(self):
        return self._items[-1] if self._items else None
    
    def is_empty(self):
        return self.peek() is None
    
    def size(self):
        return len(self._items)
    
    def __len__(self):
        return len(self._items)
    
s = Stack()
print(s.is_empty())
print(s.push(4))
print(s.push('dog'))
print(s.peek())
print(s.push(True))
print(s.size())
print(s.is_empty())
print(s.push(8.4))
print(s.pop())
print(s.pop())
print(s.size())


def balance_checker(par_str):
    open_pars = ["(","{","["]
    closed_pars = [")","}","]"]
    par_stacks = [Stack()]*3
    # Inefficient with space. You don't need the 3 stacks. But time complexity is good.

    for char in par_str:
        for i in range(3):
            if char == open_pars[i]:
                par_stacks[i].push(char)
            elif char == closed_pars[i]:
                if par_stacks[i].is_empty():
                    return False
                par_stacks[i].pop()
    
    for par_check in par_stacks:
        if not par_check.is_empty():
            return False
    return True

print(balance_checker('(([{[[({({{adas(sd([{[adf({[{[afgdsg[{({})s]dfgs)]sdfg}sdfg)s]dfg}sdf)gsd}fg}sg}])]})}]]})])'))
print(balance_checker('([(([{{({[([{(([[[[(([({(]]))]])])})]}))}}])})]]))'))
print(balance_checker('{([[({{(({(({[(((({{((([[}}])})))}}})])])))))}])])'))
print(balance_checker('5]]0fJ{dv))6}]}}{][x][sh({}{[3}(({{]]8{{[{m)30{U)}'))
print(balance_checker('3[[}[]Ai{(14}6{J7X{T]{)(6b}(T2)})]{)){5]{u6][4(j)}'))
print()

def decimal_base_converter(num, new_base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()
    while num > 0:
        rem_stack.push(digits[num % new_base])
        num //= new_base
    
    binary = ""
    while not rem_stack.is_empty():
        binary += rem_stack.pop()
    return binary

print(decimal_base_converter(233, 2))
print(decimal_base_converter(42, 2))
print(decimal_base_converter(31, 2))

print(decimal_base_converter(233, 8))
print(decimal_base_converter(233, 16))



def infix_to_postfix(infix_str):
    operators = ["(","+","-","*","/","^"]

    op_stack = Stack()
    output = []
    for tok in infix_str:
        if tok.isalnum():
            output.append(tok)
        elif tok == "(":
            op_stack.push(tok)
        elif tok == ")":
            op = op_stack.pop()
            while op != "(":
                output.append(op)
                op = op_stack.pop()
        elif tok in operators:
            while not op_stack.is_empty() and operators.index(op_stack.peek()) >= operators.index(tok):
                output.append(op_stack.pop())
            op_stack.push(tok)

    while not op_stack.is_empty():
        output.append(op_stack.pop())

    return "".join(output)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_to_postfix("A+B-C-D-E*F+G"))
print(infix_to_postfix("5 * 3 ^ (4 - 2)"))

def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

def postfix_eval(postfix):
    operands = Stack()
    for tok in postfix:
        if tok.isalnum():
            operands.push(int(tok))
        elif tok in ["+","-","*","/"]:
            op1, op2 = operands.pop(), operands.pop()
            result = do_math(tok, op2, op1)
            operands.push(result)
    
    return operands.pop()

print(postfix_eval("7 8 + 3 2 + /"))

"""
Essentially: any time you need to reverse the order of the items in your algorithm,
try using a Stack.

Another interesting idea with stacks is that, they're so good at evaluation because
they can 'hold' memory temporarily until the right operator is detected.

Try to consider that idea with language translation - you 'hold' adjectives until you
encounter a noun, you hold 'adverbs' until you encounter a verb, etc... Stacks are
great for language and even programming language translation.
"""


"""
Next up: Queues!

3.10 Queues

A queue is a linear data structure where addition and removal occur at opposite ends.
The ends are commonly called the FRONT and the END, or the head and the tail.

Think of the queue abstractly as if the rear is on the left and the front is on the right.
I.e. you're looking at the tail - that's the only place you can enter the queue from.
Think of it just like any normal queue, e.g. queuing up to order a Boost.

A real-life applications of queues is documents queued up for printing. 2 computers can queue
up multiple documents to the end of the queue, and the document at the front/head of the queue
gets actioned. Queues are also used to register key types when we type on the keyboard, and
for example the system is busy loading up a new tab on Chrome. The key presses get added to a
Queue-like buffer that can eventually be actioned and displayed on the screen.

This idea of 'scheduling' will often use queues, when we want to maintain the same order.

Queues in Python are implemented with a list, where index 0 is the rear and index -1 is the front.
E.g. [3, 2, 1] is how 1, 2, 3 would be enqueued. You can dequeue 1 easily, but 3 is costly and inefficient.

Note how unlike stacks, the order of removal is THE SAME as the order of insertion. Great for standard needs.

Stacks are used for DFS!

"""

class Queue:
    def __init__(self):
        self._items = []

    def __repr__(self):
        return f"Queue{self._items}"
    
    def __len__(self):
        return len(self._items)
    
    def size(self):
        return len(self)
    
    def is_empty(self):
        return True if len(self) == 0 else False
    
    def enqueue(self, item):
        self._items.insert(0, item)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self._items.pop()

    
print("\n~~Queues~~")
    
q = Queue()
q.enqueue(4)
q.enqueue("dog")
q.enqueue(True)
print(q.size())
print(q.is_empty())
print(q.enqueue(8.4))
print(q.dequeue())
print(q.dequeue())
print(q.size())

"""
Note! enqueue and all operations on either end become O(1) when implemented with LinkedLists.
enqueue() : O(n)
dequeue() : O(1)
search/insert : O(n)
"""

def josephus(n, k):
    romans = Queue()
    for x in range(1,n+1):
        romans.enqueue(x)
    ctr = 1
    while romans.size() > 2:
        roman = romans.dequeue()
        if ctr % k != 0:
            romans.enqueue(roman)
        ctr += 1
    
    print(f"And the winning romans are...{romans.dequeue()} and {romans.dequeue()}!")

josephus(41, 3)

"""

Essentially, think of queues as simply real-life queues. Use them when you need to queue
things up! Practical examples are task scheduling, print scheduling, and video streaming.

Queues are also great for TIMING simulations, since you can add a time to your queue
(which might represent the start), and then removing from the queue simply removes that
first time (start), which you can then compare with the time now (end) to get a simple
timer.

Queues can also be interesting in applications where a 'circular' option is needed.
Kind of like a Circular Linked List - this can be done easily with a queue by enqueuing
and dequeuing at the same time.

BFS uses Queues!

"""

"""
3.15: Deques

Pronounced 'deck'. Decks (deques) are double-ended queues, so essentially gain the functionality
of both stacks and queues. The key thing with deques is that the front and the rear MUST
be kept track of at all times and kept consistent.

Deques are pretty similar to queues in terms of time complexity, just with more operations available.
E.g. for [1, 2, 3] you can both append 4 = [1,2,3,4], pop = [1,2], appendleft 0 = [0,1,2,3], or pop(0) = [2,3].
All in O(1) time if implemented properly (with Nodes / LinkedLists).

The implementation below is a simplified version without nodes, costing O(n) to add/pop from the tail
but O(1) to add/pop from the head.
"""

class Deque:

    def __init__(self):
        self._items = []

    def __repr__(self):
        return f"Deque{self._items}"

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop() if self._items else None
    
    def remove_rear(self):
        return self._items.pop(0) if self._items else None
    
    def is_empty(self):
        return not bool(self._items)
    
    def size(self):
        return len(self._items)

    
print("\n~~~Deques~~~")

d = Deque()
print(d.is_empty())
d.add_rear(4)
d.add_rear("dog")
d.add_front("cat")
d.add_front(True)
print(d)
print(d.size())
print(d.is_empty())
d.add_rear(8.4)
print(d.remove_rear())
print(d.remove_front())

def palindrome_checker(pal):
    d = Deque()
    for char in pal:
        d.add_front(char)

    while d.size() > 1:
        if d.remove_front() != d.remove_rear():
            return False
    return True

print("\npalindromes")
print(palindrome_checker("radsa"))
print(palindrome_checker("rad"))
print(palindrome_checker("dad"))
print(palindrome_checker("detartrated"))

"""
Note that deques are really different to doubly linked lists 
(idk why I thought they were the same). Deques are just a singly linked list
with a pointer to both the head and tail.

We'll have more notes on Deques when we implement one with Nodes.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3.20: Linked Lists

The fun begins. We start with our first Node-based structure.

We'll start with a singly-linked list, where we only keep track of the head.

Okay, a big, big note we're gonna make here. From now on, all your class attributes
that you define in init should probably START WITH AN UNDERSCORE. It's good coding 
practice because it signals that the attribute is supposed to be PRIVATE, i.e. only 
changed through methods and not directly outside of the class. Gonna apply this to all 
other classes too.

The other point of this is that you begin the attributes defined in init with an 
underscore, then you're supposed to use decorators with proper getters and setters
as below to make it much simpler to update and read, while maintaining safety.

However, there's an important caveat here; you don't need to use the underscore
syntax if the attribute is DESIGNED to be edited publicly.

The LinkedList is a perfect example; Node attributes are supposed to be private, only
edited through getter and setter methods - following the conventions of ENCAPSULATION.

But the LinkedList itself will have a self.head attribute with no underscore,
precisely because the head is the public access point of the LinkedList - it's meant
to be interacted with directly.

Let's begin.
"""

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    def __repr__(self):
        return f"Node({self.value})" 

print("\n~~~Linked Lists~~~")

head = Node(0)
curr = head
for num in range(10):
    curr.next = Node(num)
    curr = curr.next

print(head)

"""
Key point: singly LinkedList addition/removal occurs at the HEAD, because that's
what we have immediate access to. O(1) implementation.

The idea of the LinkedList is to ensure the developer never has to interact with
or create a Node. They just use the LinkedList object.
"""

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        # Note that this is inefficient - simply for learning how to traverse the linkedlist.
        # Normally you'll have a 'size' attribute that is incremented or decremented when nodes
        # are added to the linked list.
        ctr = 0
        curr = self.head
        while curr:
            ctr += 1
            curr = curr.next
        return ctr

    def add(self, item):
        curr = Node(item)
        curr.next = self.head
        self.head = curr

    def search(self, item):
        curr = self.head
        while curr:
            if curr.value == item:
                return True
            curr = curr.next
        return False
    
    def __str__(self):
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        return " -> ".join(values)

# Note in remove(): if the list is empty, we don't raise an error of sorts.
# The reason why is because removing from an empty list is a feasibly common 
# operation that may occur in more complex systems, and we wouldn't want the entire 
# program to shutdown in the case of an empty list. For example, double checking that
# an item has been removed from a list would be a valid and common idea even in testing.

# If every time we called remove we needed to handle exceptions, it would make the rest
# of our codebase unnecessarily tedious and unreadable. However, obviously some lists
# might need to behave differently where all items should be carefully tracked, in which
# case you'd implement some sort of Exception/Error.

    def remove(self, item):
        curr = self.head
        if not curr:
            return
        if curr.value == item:
            self.head = curr.next
            return
        while curr.next:
            if curr.next.value == item:
                curr.next = curr.next.next
                return
            curr = curr.next
        
        raise ValueError(f"{item} is not in LinkedList.")
    
    def append(self, item):
        curr = self.head
        if not curr:
            self.head = Node(item)
            return
        while curr.next:
            curr = curr.next
        curr.next = Node(item)

    def insert(self, item, idx):
        if idx < 0:
            raise IndexError(f"Index cannot be negative.")
        
        new_node = Node(item)
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        curr = self.head
        curr_idx = 0
        while curr:
            if curr_idx == idx-1:
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next
            curr_idx += 1

        raise IndexError(f"Index {idx} out of range.")

    def pop(self, idx=None):
        if idx is None:
            if self.size() == 0:
                return None
            idx = self.size() - 1
        if idx < 0:
            raise IndexError(f"Index cannot be negative.")
        
        curr = self.head
        if idx == 0:
            self.head = self.head.next
            return curr.value

        curr_idx = 0
        while curr.next:
            if curr_idx == idx-1:
                result = curr.next.value
                curr.next = curr.next.next
                return result
            curr = curr.next
            curr_idx += 1

        raise IndexError(f"{idx} out of range.")    

    def index(self, idx):
        if idx < 0:
            raise IndexError(f"Index cannot be negative.")

        curr_idx = 0
        curr = self.head
        while curr:
            if curr_idx == idx:
                return curr.value
            curr = curr.next
            curr_idx += 1

        raise IndexError(f"Index cannot be negative.")

my_list = LinkedList()

my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

print(my_list.size())
print(my_list.search(93))
print(my_list.search(100))

my_list.add(100)
print(my_list.search(100))
print(my_list.size())
print(my_list)

my_list.remove(54)
print(my_list.size())
my_list.remove(93)
print(my_list.size())
my_list.remove(31)
print(my_list.size())
print(my_list.search(93))

try:
    my_list.remove(27)
except ValueError as ve:
    print(ve)

ll = LinkedList()
ll.insert(10, 0)  # Insert 10 at index 0
ll.insert(20, 1)  # Insert 20 at index 1
ll.insert(30, 1)  # Insert 30 at index 1

print(ll.index(1))  # Expected: 30
print(ll.pop(0))  # Expected: 10
print(ll.pop(1))  # Remove 20


"""
3.22: Sorted Lists

This time we're gonna make a special kind of LinkedList.
It's gonna be a List sorted ascendingly by number.
Adding becomes more expensive because we can't just append or prepend anymore.

Let's go.
"""

class SortedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"SortedList{self.head}"
    
    def add(self, item):
        curr = self.head
        new_node = Node(item)
        if not curr or curr.value >= item:
            self.head = new_node
            new_node.next = curr
            return

        while curr.next and curr.next.value < item:
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node

    def remove(self, item):
        if not self.head:
            return
        if self.head.value == item:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next:
            if curr.next.value == item:
                curr.next = curr.next.next
                return
            curr = curr.next
        
        raise ValueError(f"{item} not found in SortedList.")
    
    def search(self, item):
        curr = self.head
        while curr:
            if curr.value == item:
                return True
            if curr.value > item: # Early exit :D
                return False
            curr = curr.next
        
        return False
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        curr = self.head
        ctr = 0
        while curr:
            ctr += 1
            curr = curr.next
        return ctr

    def index(self, item):
        curr = self.head
        idx = 0
        while curr:
            if curr.value == item:
                return idx
            curr = curr.next
            idx += 1
        
        raise ValueError(f"{item} not in list.")
    
    def pop(self, idx=None):
        if idx is None:
            if self.size() == 0:
                return None
            idx = self.size() - 1
        if idx < 0:
            raise IndexError(f"Index cannot be negative.")
        
        curr = self.head
        if idx == 0:
            self.head = self.head.next
            return curr.value

        curr_idx = 0
        while curr.next:
            if curr_idx == idx-1:
                result = curr.next.value
                curr.next = curr.next.next
                return result
            curr = curr.next
            curr_idx += 1

        raise IndexError(f"{idx} out of range.")           

    def __str__(self):
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        return " -> ".join(values)

print(f"~~~SortedLists~~~")

# Testing the SortedList
sl = SortedList()
sl.add(5)
sl.add(1)
sl.add(3)
sl.add(2)
sl.add(4)

print(sl.search(3))  # Expected: True
sl.remove(3)
print(sl.search(3))  # Expected: False
print(sl.search(6))  # Expected: False
print(sl.size())  # Expected: 4
print(sl.index(2))  # Expected: 1
print(sl.pop())  # Expected: 5 (largest)
print(sl.pop(1))  # Expected: 2
print(sl.pop()) # Expected: 4
print(sl.pop()) # Expected: 1

"""
SortedLists are interesting. Because they essentially cost O(n) to do almost every operation,
but they maintain the order such that retrieving the min is O(1). If you add a tail pointer too
(as in a Sorted Doubly Linked List), retrieving both the min and max is O(1). Can have some
interesting applications.

Just to clarify, for SortedLists:
- add(item): O(n)
- remove(item): O(n)
- index(item): O(n)
- pop(index=-1): O(n)
- search(item): O(n)
- size(): O(n) or O(1) with efficient attribute.

So basically O(n) for everything.

Realistically, the lack of efficiency makes this data structure rarely used, but it's a good
introduction to things like min and max heaps.

Now, what you may have noticed with these Linked List operations is that
the obvious special case to handle is modification to the head of the linked list.
Once we introduce tails, that will also be a special case.

It'll typically be: 
- check input parameter is correct (e.g index out of range)
- check linked list isn't empty
- handle modification to 1 node in list (head = tail)
- handle modification to head node
- handle modification to tail node

"""

# Exercises

print(decimal_base_converter(17, 2))
print(decimal_base_converter(45, 2))
print(decimal_base_converter(96, 2))

print(infix_to_postfix("(A+B)*(C+D)*(E+F)"))
print(infix_to_postfix("A+((B+C)*(D+E))"))
print(infix_to_postfix("A*B*C*D+E+F"))

print(postfix_eval("2 3 * 4 +"))
print(postfix_eval("1 2 + 3 + 4 + 5 +"))
print(postfix_eval("1 2 3 4 5 * + * +"))


def html_checker(html): # Assuming tag arrows are correct/simple in the input.
    tags = Stack()
    tag = ""
    opening = None  # Cycle between None, True and False for different scanning states
    # IN RETROSPECT: try to look for a non-state solution with simple problems first,
    # because it adds a layer of complexity. But arguably states are good for more difficult
    # problems, i.e. LeetCode Mediums and Hards so keep them in the bank.
    for char in html:
        if char == "<":
            opening = True
        elif char == "/" and opening is True:
            opening = False
        elif char == ">":
            if opening is True:
                tags.push(tag)
            elif opening is False:
                if tags.pop() != tag:
                    return False
            tag = ""
            opening = None
        elif char.isalpha():
            if opening is not None:
                tag += char
    
    return tags.is_empty()

html_str = """
<html>
   <head>
      <title>
         Example
      </title>
   </head>

   <body>
      <h1>Hello, world</h1>
   </body>
</html>
"""
print(f"HTML was checked and returned {html_checker(html_str)}.")

def palindrome_checker_spaces(pal):
    d = Deque()
    for char in pal:
        if char.isalpha():
            d.add_front(char)

    while d.size() > 1:
        if d.remove_front() != d.remove_rear():
            return False
    return True

palindrome_spaces = "I PREFER PI"
print(f"{palindrome_spaces} was checked as a palindrome and returned {palindrome_checker_spaces(palindrome_spaces)}.")


class NodeQueue:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0
    
    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) if values else "Queue is empty."
    
    def enqueue(self, item):
        new_node = Node(item)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        
    def dequeue(self):
        if not self.head:
            raise IndexError("Queue is empty.")
        result = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        return result

print("\n~~NodeQueues~~")
    
q = NodeQueue()
q.enqueue(4)
q.enqueue("dog")
q.enqueue(True)
print(q)
print(q.size)
print(q.size == 0)
print(q.enqueue(8.4))
print(q.dequeue())
print(q.dequeue())
print(q)
print(q.size)

"""
Queue with O(1) enqueue and O(1) dequeue implemented.

Key thing to notice is that the self.head is on the 'left' instead of the right
as compared to just using Python lists.

Next up: DoublyLinkedList.
"""

class DNode:
    def __init__(self, value):
        self._value = value
        self._next = self._prev = None

    def __repr__(self):
        return f"Node({self._value})"

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, next):
        self._next = next

    @property
    def prev(self):
        return self._prev
    
    @prev.setter
    def prev(self, prev):
        self._prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0
    
    def __repr__(self):
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        return ", ".join(values) if values else "DoublyLinkedList is empty."
    
    def prepend(self, item):
        new_node = DNode(item)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def append(self, item):
        new_node = DNode(item)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def search(self, item):
        curr = self.head
        while curr:
            if curr.value == item:
                return True
            curr = curr.next

        return False

    def index(self, idx):
        if idx < 0:
            raise IndexError("Can't have negative index.")
        if not self.head:
            raise IndexError("List is empty.")
        if idx >= self.size:
            raise IndexError(f"Index {idx} out of range for size {self.size}.")
        
        curr = self.head
        curr_idx = 0
        while curr_idx != idx:
            curr = curr.next
            curr_idx += 1
        return curr.value            

    def remove(self, item):
        if not self.head:
            raise IndexError("List is empty.")
        
        curr = self.head
        while curr:
            if curr.value == item:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next  # Removing head

                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev  # Removing tail

                self.size -= 1
                return True
            curr = curr.next

        raise ValueError(f"Item {item} not found in list.")

    def pop(self, idx=None):
        if not self.head:
            raise IndexError("List is empty.")
        if idx < 0:
            idx = self.size + idx
        if idx < 0 or idx >= self.size:
            raise IndexError("Index out of range.")
        
        curr = self.head
        for _ in range(idx):
            curr = curr.next

        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev

        self.size -= 1
        return curr.value