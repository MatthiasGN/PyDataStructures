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


my_maze = Maze("maze2.txt")
my_maze.draw_maze()
my_maze.update_position(my_maze.start_row, my_maze.start_col)

search_from(my_maze, my_maze.start_row, my_maze.start_col)