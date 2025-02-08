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

Let's compare to another stack solution:
"""

from pythonds3.basic import Stack

def to_str(n, base):
    r_stack = Stack()
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n % base])
        n = n // base
    res = ""
    while not r_stack.is_empty():
        res = res + str(r_stack.pop())
    return res


print(to_str(1453, 16))
print(to_str(100, 10))

"""
This example gives an insight onto what we call the STACK FRAME.
The stack frame is essentially what Python uses to handle the local variables of a function.
So in a recursive function, each function call is added to the stack frame until we reach the base case,
which equates to a result instead of a function call, and that result is added to the top of the stack frame.

Try to think about it abstractly - we use a stack because we also need its reversal ability.
Each function call is added to the stack, so that the last stack call becomes the first part of the result (LIFO!).

This 'call stack' actually ends up adding to the SPACE COMPLEXITY!

Because otherwise, in a sense recursion would be way too much of a hack - seemingly O(1) space complexity for pretty much
all recursive functions, when in reality that often isn't possible.

A simpler example of reversing a string:
"""

def reverse_str(str):
    if len(str) == 1:
        return str
    return str[-1] + reverse_str(str[:-1])

print(reverse_str("tester"))
    

"""
Simpler palindrome without stacks:
"""
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

assert is_pal(remove_white("x")) is True
assert is_pal(remove_white("radar")) is True
assert is_pal(remove_white("hello")) is False
assert is_pal(remove_white("")) is True
assert is_pal(remove_white("hannah")) is True
assert is_pal(remove_white("madam i'm adam")) is True

"""
Before we get to the next part here, just adding a big note here on ENVIRONMENTS.

In the context of programming, an environment typically refers to the combination of
tools, libraries and settings that enable a program or application to run. This may 
include runtime libraries / modules, language versions, dependencies, packages, and
configuration settings.

However, some programming languages don't require environments. For example, C, C++,
assembly code (probably) are low level enough to not require them.

On the other hand, languages like Python, JavaScript, Java, C#, etc all require and
use an environment.

The useful thing about environments is that you have the system-wide environment which
is the default environment used when you install an environment-dependent programming
language, e.g. Python. This include the default Python version and system-wide libraries
such as string, random, sys, etc.

However, IDEs such as Visual Studio Code here allow us to create VIRTUAL ENVIRONMENTS.
Virtual environments are super useful and often used in the professional world because
they are ISOLATED from the global environment. So for example, you could run a file using
an environment with an earlier version of Python and completely different packages, or you
could run the same file with a modern and up-to-date virtual environment with thousands
of packages.

The other great thing about virtual environments is that you can easily share the exact
environment configurations with team members, allowing them to exactly replicate the
packages and dependencies you use for a given project / file.

Isolation is also just generally better for safety / security, since you reduce the risk
of breaking the system-wide tools and libraries. You can also test libraries or upgrades
without impacting other projects.


Now, alongside environments we also have PACKAGE MANAGERS. For example, Homebrew is a
package manager for macOS (and Linux) used to install, update and manage system-wide
software. You could say it helps to manage the system-wide environment, but it is not 
actually 'required'. It is very useful because it tracks and maintains the system
dependencies for your global environment.

Now pip3 on the other hand is actually ALSO a system-wide package manager, but it ONLY
manages Python packages. So you can use it to install python packages system wide or 
only in your local environment, allowing you to customise package dependencies.


Package managers are essentially one role often filled within the system-wide environment.
But we also have more broad tools like BUILD TOOLS. Examples of build tools include Gradle
and Maven for Java, and Make or CMake for C/C++. Build tools essentially do package management
among a bunch of other roles such as source code compilation, linking libraries, running tests,
and actually deploying the application.

The reason why build tools are needed for languages such as Java and C is because compared to
Python, much more of the compilation / building process is modifiable by the user for greater
security and efficiency (from an entire programming language perspective). For example,
Python handles pretty much all the compilation and execution in its Interpreter, whereas
C has a separate compiler (often GCC), preprocessor, assembler and executor.


To create a virtual environment in Python, navigate to the home directory of your project then do:

> python3 -m venv venv

That'll create a virtual environment in the 'venv' folder, which will be used to define and track
the dependencies, packages, and modules you use for that project. Then you need to activate it using:

> source venv/bin/activate

Once activated, you'll see the name of your virtual environment (venv) in terminal. From there,
you need to DEACTIVE and ACTIVATE the NEW virtual environment every time you switch projects.

> deactivate

The good thing is, VSCode handles most of this on its own when you open a new window/project.

Final thing to add here is that you can often see a (base) at the start of your terminal command line.
This refers to the ANACONDA base environment. You generally do NOT want to be using multiple environments,
because it can make things confusing as to which environment has which packages and kind of loses the
benefits of isolation. To deactivate the anaconda environment, use:

> conda deactivate

You can also deactivate both if you're in a simple terminal to return to your global Python environment.


Another really useful thing to add here - you may remember always having issues with setting the PATH
variable when starting with Python. This directly relates to everything we've discussed here -
the PATH variable is an ENVIRONMENT VARIABLE; it contains a list of paths (directories) that the system
looks through to find executables, dependencies, packages, modules, and so on.

And actually, when you activate a virtual environment, it MODIFIES the PATH temporarily to point to the
virtual environment's versions of Python and other tools!

The PATH environment variable is pretty important - if PATH is empty or deleted, the system won't know
where to look for all its programs, so any command you try to run in terminal will fail. Shell commands
like ls, cd and so on will also fail. So, be very careful with it!


Anyway, to summarise here, you should use a virtual environment for every different project you have.
"""


"""
4.7 Visualizing Recursion
"""

import turtle

# def draw_spiral(my_turtle, line_len):
#     if line_len > 0:
#         my_turtle.forward(line_len)
#         my_turtle.right(40)
#         draw_spiral(my_turtle, line_len-2)

# my_turtle = turtle.Turtle()
# my_win = turtle.Screen()
# draw_spiral(my_turtle, 100)
# my_win.exitonclick()

"""
Pretty cool.

And honestly one of the coolest uses of recursions I've ever seen: FRACTALS.
"""

def tree(branch_len, t):
    if branch_len > 10:
        t.pensize(branch_len / 75 * 20)
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 7, t)
        t.left(40)
        tree(branch_len - 7, t)
        t.right(20)
        # t.color("brown")
        # if branch_len < 20:
        #     t.color("green")
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    t.speed(0)
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    # t.color("brown")
    tree(75, t)
    my_win.exitonclick()
# main()

"""
What this should make you realise is that Recursion is basically just a Depth First Search!

The reason why is because similarly to Stacks, they are both Last-In-First-Out (LIFO)!
The last thing you add is the first thing you evaluate!

To be honest, the best way to think about recursion is like a STACK.

Some more actually awesome Turtle examples. We start with the Sierpinski Triangle, another fractal.
"""

def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()


def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, my_turtle):
    colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange"]
    draw_triangle(points, colormap[degree], my_turtle)
    if degree > 0:
        sierpinski(
            [points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])],
            degree - 1,
            my_turtle,
        )
        sierpinski(
            [points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])],
            degree - 1,
            my_turtle,
        )
        sierpinski(
            [points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])],
            degree - 1,
            my_turtle,
        )


def main():
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    my_win = turtle.Screen()
    my_points = [[-180, -150], [0, 150], [180, -150]]
    print(my_points)
    sierpinski(my_points, 5, my_turtle)
    my_win.exitonclick()

# main()

"""
Realising somethere here. When you watch this implementation, this is a DFS drawing of a fractal.
But it should absolutely be possible to achieve the same thing with a BFS, i.e. drawing the bigger
triangles before the smaller ones. I wonder if you'd still use recursion or not... you could probably
do it both with and without it.

Either way, TURTLE programming is elite.

Next problem: Tower of Hanoi
"""

def tower_of_hanoi(n, from_tower, with_tower, to_tower, towers):
    if n == 1:
        disk = towers[from_tower].pop()
        towers[to_tower].append(disk)
        print(f"A: {str(towers['A']):<{max_width}}, B: {str(towers['B']):<{max_width}}, C: {str(towers['C']):<{max_width}}")
        return

    tower_of_hanoi(n - 1, from_tower, to_tower, with_tower, towers)

    disk = towers[from_tower].pop()
    towers[to_tower].append(disk)
    print(f"A: {str(towers['A']):<{max_width}}, B: {str(towers['B']):<{max_width}}, C: {str(towers['C']):<{max_width}}")

    tower_of_hanoi(n - 1, with_tower, from_tower, to_tower, towers)

num_disks = 4
towers = {
    "A": list(range(num_disks, 0, -1)),  # Disks in descending order
    "B": [],
    "C": []
}

max_width = max(len(str(towers[peg])) for peg in towers)
print("\n~~~Towers of Hanoi~~~")
print(f"A: {str(towers['A']):<{max_width}}, B: {str(towers['B']):<{max_width}}, C: {str(towers['C']):<{max_width}}")

tower_of_hanoi(num_disks, "A", "B", "C", towers)

"""
Pretty cool. Main thing to note here is that if you weren't using recursion,
you'd just use a stack for each tower. But that's precisely the point -
recursion uses CALL STACKS.

Next up: Exploring a Maze.
"""


START = "S"
OBSTACLE = "+"
TRIED = "."
DEAD_END = "-"
PART_OF_PATH = "O"


class Maze:
    def __init__(self, maze_filename):
        with open(maze_filename, "r") as maze_file:
            self.maze_list = [
                [ch for ch in line.rstrip("\n")]
                for line in maze_file.readlines()
            ]
        self.rows_in_maze = len(self.maze_list)
        self.columns_in_maze = len(self.maze_list[0])
        for row_idx, row in enumerate(self.maze_list):
            if START in row:
                self.start_row = row_idx
                self.start_col = row.index(START)
                break

        self.x_translate = -self.columns_in_maze / 2
        self.y_translate = self.rows_in_maze / 2
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(
            -(self.columns_in_maze - 1) / 2 - 0.5,
            -(self.rows_in_maze - 1) / 2 - 0.5,
            (self.columns_in_maze - 1) / 2 + 0.5,
            (self.rows_in_maze - 1) / 2 + 0.5,
        )

    def draw_maze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(
                        x + self.x_translate, -y + self.y_translate, "orange"
                    )
        self.t.color("black")
        self.t.fillcolor("blue")
        self.wn.update()
        self.wn.tracer(1)

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_bread_crumb(self, color):
        self.t.dot(10, color)

    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTACLE:
            color = "red"
        elif val == TRIED:
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None

        if color:
            self.drop_bread_crumb(color)

    def is_exit(self, row, col):
        return (
            row == 0
            or row == self.rows_in_maze - 1
            or col == 0
            or col == self.columns_in_maze - 1
        )

    def __getitem__(self, idx):
        return self.maze_list[idx]


def search_from(maze, start_row, start_column):
    # try each of four directions from this point until we find a way out.
    # base Case return values:
    #  1. We have run into an obstacle, return false
    maze.update_position(start_row, start_column)
    if maze[start_row][start_column] == OBSTACLE:
        return False
    #  2. We have found a square that has already been explored
    if (
        maze[start_row][start_column] == TRIED
        or maze[start_row][start_column] == DEAD_END
    ):
        return False
    # 3. We have found an outside edge not occupied by an obstacle
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True
    maze.update_position(start_row, start_column, TRIED)
    # Otherwise, use logical short circuiting to try each direction
    # in turn (if needed)
    found = (
        search_from(maze, start_row - 1, start_column)
        or search_from(maze, start_row, start_column - 1)
        or search_from(maze, start_row + 1, start_column)
        or search_from(maze, start_row, start_column + 1)
    )
    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
    return found


# my_maze = Maze("maze2.txt")
# my_maze.draw_maze()
# my_maze.update_position(my_maze.start_row, my_maze.start_col)

# search_from(my_maze, my_maze.start_row, my_maze.start_col)

"""
Elite. Note how we check each base case first, then check all the recurrences.

That brings us to the next bit of fun.

4.12 Dynamic Programming

We start off with the classic problem of fewest coin denominations. For example,
if I'm owed $3.80, what's the fewest coins that can satisfy that amount?
Well, it'd be:
- $2 x 1
- $1 x 1
- 50c x 1
- 20c x 1
- 10c x 1
= 5 coins.

We basically just choose the biggest coin we can at each step.
This idea of always choosing the 'best' option at each recursive step is called a
GREEDY algorithm. We know these well, but lots more on that later.

However, what if we introduced a new denomiation of coin, e.g. 40c?

All of a sudden, our greedy algorithm doesn't find the most optimal solution, since
the new optimal becomes:
- $2 x 1
- $1 x 1
- 40c x 2
= 4 coins.

So even though 40c is less than 50c, it's more optimal.
As such, we need to find a new solution: Dynamic Programming.

As similar to the maze problem, we start with our base cases, then we set up a
RECURRENCE RELATION. To set this up, we essentially think of all the possible
paths towards the optimal solution within the recursive function and make an
equation out of it. In this case, we have:
num_coins = min(
    1 + num_coins(original_amount - 5c)
    1 + num_coins(original_amount - 10c)
    1 + num_coins(original_amount - 20c)
    1 + num_coins(original_amount - 40c) # Our new case
    1 + num_coins(original_amount - 50c)
    1 + num_coins(original_amount - $1)
    1 + num_coins(original_amount - $2)
)

An example function is implemented below:
"""

recursions = 0
def make_change_dnc(coin_denoms, change):
    global recursions
    recursions += 1
    if change in coin_denoms:
        return 1
    if change > 0:
        min_coins = float("inf")
        for i in [c for c in coin_denoms if c <= change]:
            num_coins = 1+make_change_dnc(coin_denoms, change - i)
            min_coins = min(num_coins, min_coins)
        return min_coins
    
print(make_change_dnc([1,5,10,25], 42))
print(f"{recursions} recursions!")

"""
However, what you may notice is that this is incredibly inefficient.
The number of recursive calls actually becomes EXPONENTIAL.
For example, with the example of 4 coin denominations and a target of 42,
we end up with O(4^n) = O(4^42) recursions in the worst case!
Given that we have the average case here, it takes 108,534 recursions.

Super inefficient. Now, you may have also realised something - this isn't
actually dynamic programming yet. It's just brute force recursion with backtracking.
The reason why is because we're not using DP's special tools: tabulation and memoization.
We're just exponentially dividing the problem down into smaller subproblems.

To give you an understanding of why this is so inefficient, consider that
when trying to solve this problem with a target of 42, we would feasibly have
to recurse to the smaller target of 12 in multiple ways - for example, 42 minus
10c minus 10c minus 10c, or replace any of those with minus 5c x 2. However,
each time we get to this same target, WE'RE RECALCULATING THE RESULT THROUGH
RECURSION EACH TIME, even though WE'VE ALREADY CALCULATED IT BEFORE.

So to solve this issue, we need to store the result of previous calculations.
A simple way to do this with dynamic programming is to store them in a table!

Let's have a look:
"""
recursions = 0
def make_change_2(coin_value_list, change, known_results):
    global recursions
    recursions += 1
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + make_change_2(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
            known_results[change] = min_coins
    return min_coins

print("\n~~~~~~~~Dynamic Programming~~~~~~~~")
print(make_change_2([1, 5, 10, 25], 42, [0] * 43))
print(f"{recursions} recursions!")

"""
How insane is that. We've gone from 108,534 recursions to just 122 !!

Now note that even though we're using a table, THIS IS NOT TABULATION.
This is instead called MEMOIZATION (or CACHING). The reason why is because 
memoization refers to top-down dynamic programming (i.e. start at biggest problem
and divide them down from there), while tabulation refers to bottom-up
dynamic programming (i.e. solve the subproblems first, then solve the
biggest problem without recursion).

To understand this a bit better, let's go into a bit more depth on memoization.
What you'll note is that the results table is initially just a table of zeroes,
i.e. empty. Then as the function recursively calls and finds a result that isn't
in the table, it adds that result AS NEEDED. At the end of all recursions, the
table may not even be fully filled in - for example, if 1 was not a coin
denomination there would feasibly be many holes in the table, e.g. calculating the
change required for 39 would never be needed.

In contrast, tabulation does this all the other way. It actually starts by FILLING
OUT the table, which is what takes up the bulk of our solution, allowing us to simply
call the solution needed at the end. There are NO HOLES in the table - if we wanted
to then find the solution to a smaller number, we are guaranteed to have it and be
able to return it in O(1).

In particular, filling out the table with tabulation DOES NOT REQUIRE RECURSION.
That is the major difference between the two - memoization uses recursion,
while tabulation does not.

A final thing to note is that in our above solution, we pass the result table
through the recursions. The other, possibly simpler but less safe/modular/clean way
to implement this is with a global memoization variable, i.e. a dictionary
created outside the function but edited from within.

With all that said, let's take a look at the tabulation DP solution:
"""

operations = 0
def make_change_tab(coin_value_list, change):
    global operations
    # Initialize DP table with a large number (inf means no solution found yet)
    dp = [float("inf")] * (change + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    # Compute the minimum coins required for each amount up to 'change'
    for amount in range(1, change + 1):
        for coin in coin_value_list:
            operations += 1
            if coin <= amount:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    return dp[change] if dp[change] != float("inf") else -1  # Return -1 if no solution

print(make_change_tab([1, 5, 10, 25], 42))
print(f"{operations} operations!")

"""
168 operations to 122 recursions. Fairly similar. What should be noted is that each recursion
actually has a fair few operations within, so the actual number of operations for the memoization
example above is 200+. We call this the RECURSION OVERHEAD.

As such, if we really want to maximise efficiency we should always aim to find a tabulation solution
first, then only move to memoization if that's too difficult / not possible.

Anyway, the major takeaway from this chapter is that although recursion can often be used to simplify
or speed up solutions, it is not always the most efficient answer.

Let's print out the final dp so we can investigate DP tabulation in a bit more depth.
"""

dp = [float("inf")] * (42 + 1)
def make_change_tab(coin_value_list, change):
    global dp
    # Initialize DP table with a large number (inf means no solution found yet)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    # Compute the minimum coins required for each amount up to 'change'
    for amount in range(1, change + 1):
        for coin in coin_value_list:
            if coin <= amount:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    return dp[change] if dp[change] != float("inf") else -1  # Return -1 if no solution

print(make_change_tab([1, 5, 10, 25], 42))
print(dp)

"""
4.15 Exercises
"""

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n*factorial_recursive(n-1)

print(f"Factorial of 10 is {factorial_recursive(10)}.")


def reversal_recursive(ls):
    if len(ls) <= 1:
        return ls
    return reversal_recursive(ls[1:]) + [ls[0]] 
# Note that recursive reversal is inefficient due to slicing. 
# O(n^2) whereas O(n) is possible with two pointers.
    
print(f"Reversal of list [1, 2, 3, 4] is {reversal_recursive([1,2,3,4])}.")

iterations = 0
def fibonacci(n):
    global iterations
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        iterations += 1
        temp = a
        a = b
        b = temp + b
    return b

iterations2 = 0
def fibonacci_recursive(n):
    global iterations2
    iterations2 += 1
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(f"Fibonacci number 10 is {fibonacci(10)} with iteration ({iterations} iterations) and {fibonacci_recursive(10)} with recursion ({iterations2} iterations).")

"""
Relevant note here.

Firstly, you're dumb. Took way too long to get the iterative fibonacci.
Second, the recursive fibonacci ends up being O(2^n), as compared to O(n) in iterative.
9 iterations compared to 177!

Why?

Because again, it's just brute-force recursion without memoization/tabulation.

Let's try a DP solution. DP with tabulation.
"""
iterations3 = 0
    
def fibonacci_dp(n):
    global iterations3
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for num in range(2, n+1):
        iterations3 += 1
        dp[num] = dp[num-1] + dp[num-2]
    
    return dp[n]

print(f"Fibonacci number 10 is {fibonacci_dp(10)} with dynamic programming ({iterations3} iterations).")

"""
Much better. But I think this brings up an important point; for simple problems, simple iteration is often
most effective. As long as it's efficiently implemented.

Try to use recursion with dynamic programming or some other algo (divide and conquer, DFS, etc) to make it
efficient.
"""