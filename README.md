# PyDataStructures
What is used to organise, edit and manipulate data in Python.


---
### Classification
Classified as either **primitive** or **non-primitive**. Easiest differentiation is that non-primitive data types can hold primitive data types, but the opposite isn't true.

![Python Data Structure Flow Chart (from GEEKedu)](/img/ds-flowchart.png?raw=true "PyDataStructures-Flowchart")
\
<sub><sup>Rights reserved to GeeksForGeeks</sup></sub>

---
### User Defined Data Structures
These are the focus of this repository. User defined data structures are non-primitive, and also not directly supported by Python but can be built fairly simply. First, some concepts:
- First-In/First-Out (**FIFO**): the first element is processed first and the newest added element is processed last. E.g. **queue**
- Last-In/First-Out (**LIFO**): also known as FILO. The first element is processed last and the newest added element is processed first. E.g. tennis balls in a can, **stack**
- Data structures are either linear (array, queue, etc) or non-linear (graph, tree, etc).
- Static vs Dynamic: the size of a static structure is fixed while the size of a dynamic structure is variable. Static = faster access, dynamic = slower. Most data structures are dynamic besides arrays.


---
### Stack

![Stack Data Structure (from GeeksForGeeks)](/img/stack.png?raw=true "Queue")
\
<sub><sup>Rights reserved to GeeksForGeeks</sup></sub>

- Linear, LIFO
- Access: O(n)
- Search: O(n)
- Insert: O(1)
- Delete: O(1)
- Push: insert to top of stack
- Pop: remove from top of stack


---
### Queue

![Queue Data Structure (from GeeksForGeeks)](/img/Queue.png?raw=true "Queue")
\
<sub><sup>Rights reserved to GeeksForGeeks</sup></sub>

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

![Singly Linked List Data Structure (from GeeksForGeeks)](/img/single-linked-list.png?raw=true "singly-linked-list")
\
<sub><sup>Rights reserved to GeeksForGeeks</sup></sub>


#### Doubly Linked List
Each node contains references to previous and next node in sequence. Requires more memory, but can traverse backwards and forwards.

![Doubly Linked List Data Structure (from GeeksForGeeks)](/img/doubly-linked-list.png?raw=true "doubly-linked-list")
\
<sub><sup>Rights reserved to GeeksForGeeks</sup></sub>

#### Circular Linked List
The tail node points back to the head node. If implemented as a doubly linked list, the head's previous also points to the tail.

![Circular Linked List Data Structure (from GeeksForGeeks)](/img/circular-linked-list.png?raw=true "circular-linked-list")
\
<sub><sup>Rights reserved to GeeksForGeeks</sup></sub>


---
### Tree
Moving on to the non-linear data structures, a tree consists of a root node from which other nodes can branch to all the way to the leaf nodes. Thanks to their structure they often have better **time complexity** for data operations.

![Tree Data Structure (from GeeksForGeeks)](/img/tree-data-structure.png?raw=true "tree-data-structure")
\
<sub><sup>Rights reserved to GeeksForGeeks</sup></sub>

We introduce new terminology. Think of it as a family tree:
- Parent & Child Nodes
- Root Node
- Leaf or External Nodes
- Ancestor and Descendant Nodes (i.e. parent nodes, parents of parent nodes, children of children)
- Sibling nodes (same parent node)


And some general terminology:
- Subtree: any sub-section of the tree where all nodes have a common ancestor
- **Level/depth of a node**: the number of edges between this node and the root node
- **Degree of a node**: total number of subtrees attached to that node not including itself

\
Trees are commonly **binary**, so each node can have max 2 children. We also have:
- **Ternary** trees: at most 3 children nodes
- **N-ary** or **Generic** trees: no children limit

![Binary Tree (from GeeksForGeeks)](/img/binary-tree.png?raw=true "binary-tree")
\
<sub><sup>Rights reserved to GeeksForGeeks</sup></sub>

There are many more types of trees you will learn about; binary search trees, AVL trees, red-black trees, splay trees, cartesian trees, etc. Each has their own use and you should learn them.


---

Learnt and summarised from GeeksForGeeks.


