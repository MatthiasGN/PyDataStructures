# PyDataStructures
What is used to organise, edit and manipulate data in Python.

---
### Classification
Classified as either **primitive** or **non-primitive**. Easiest differentiation is that non-primitive data types can hold primitive data types, but opposite is not true.

![Python Data Structure Flow Chart (from GEEKedu)](/PyDataStructures-Flowchart.png?raw=true "PyDataStructures-Flowchart")


---
### User Defined Data Structures
These are the focus of this repository. User defined data structures are non-primitive, and also not directly supported by Python but can be built fairly simply. First, some concepts:
- First-In/First-Out (**FIFO**): the first element is processed first and the newest added element is processed last. E.g. **queue**
- Last-In/First-Out (**LIFO**): also known as FILO. The first element is processed last and the newest added element is processed first. E.g. tennis balls in a can, **stack**
- Data structures are either linear (array, queue, etc) or non-linear (graph, tree, etc).
- Static vs Dynamic: the size of a static structure is fixed while the size of a dynamic structure is variable. Static = faster access, dynamic = slower. Most data structures are dynamic besides arrays.

---
### Stack

![Stack Data Structure (from GeeksForGeeks)](/stack.png?raw=true "Queue")

- Linear, LIFO
- Access: O(n)
- Search: O(n)
- Insert: O(1)
- Delete: O(1)
- Push: insert to top of stack
- Pop: remove from top of stack




---
### Queue

![Queue Data Structure (from GeeksForGeeks)](/Queue.png?raw=true "Queue")

- Linear, FIFO
- Access: O(n)
- Search: O(n)
- Insert: O(1)
- Delete: O(1)
- Enqueue: append to end of queue
- Dequeue: pop from beginning of queue


---
### Linked List

- Linear, FIFO
- Access: O(n)
- Search: O(n)
- Insert: O(1)
- Delete: O(1)


Linked lists are similar to arrays but are created with Nodes. They are dynamic and more memory efficient since the size increases or decreases dynamically as new data is added and removed. Insertion and deletion is also far simpler as you know. There are three types of linked list:
1. Singly Linked List
2. Doubly Linked List
3. Circular Linked List

#### Singly Linked List
Each node contains a reference to the next node in sequence. Can only traverse forwards.

![Singly Linked List Data Structure (from GeeksForGeeks)](/single-linked-list.png?raw=true "singly-linked-list")

#### Doubly Linked List
Each node contains references to previous and next node in sequence. Requires more memory, but can traverse backwards and forwards.

![Doubly Linked List Data Structure (from GeeksForGeeks)](/doubly-linked-list.png?raw=true "doubly-linked-list")

#### Circular Linked List
The tail node points back to the head node. If implemented as a doubly linked list, the head's previous also points to the tail.

![Circular Linked List Data Structure (from GeeksForGeeks)](/circular-linked-list.png?raw=true "circular-linked-list")





---

All credits and rights to GeeksForGeeks.com


