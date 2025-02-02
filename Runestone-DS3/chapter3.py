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
        self.items = []

    def __repr__(self):
        return f"Stack{self.items}"

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None
    
    def peek(self):
        return self.items[-1] if self.items else None
    
    def is_empty(self):
        return self.peek() is None
    
    def size(self):
        return len(self.items)
    
    def __len__(self):
        return len(self.items)
    
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
        self.items = []

    def __repr__(self):
        return f"Queue{self.items}"
    
    def __len__(self):
        return len(self.items)
    
    def size(self):
        return len(self)
    
    def is_empty(self):
        return True if len(self) == 0 else False
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop()

    
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
enqueue() : O(n)
dequeue() : O(1)
search/insert : O(n)

Queues aren't actually that efficient!
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

BFS uses Queues!

"""

"""
Next up: Deques!

3.15: Deques

Pronounced 'deck'. Decks (deques) are double-ended queues, so essentially gain the functionality
of both stacks and queues. They're interesting because you can choose which end should be
the front and the rear (which must be kept consistent) in order to maximise efficiency.

One of the ends will be O(1) to add/remove from, and the other end will be O(n).
Like queues, the tail end is on the left of the list, e.g. for [1, 2, 3], 1 as at the tail.

In that sense

"""

class Deque:

    def __init__(self):
        self.items = []

    def __repr__(self):
        return f"Deque{self.items}"

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop() if self.items else None
    
    def remove_rear(self):
        return self.items.pop(0) if self.items else None
    
    def is_empty(self):
        return not bool(self.items)
    
    def size(self):
        return len(self.items)
    
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