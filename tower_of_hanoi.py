import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Tower of Hanoi")

# Create a list of rods and disks
rods = {'left': [], 'middle': [], 'right': []}
disks = []
rod_heights = {'left': -200, 'middle': -200, 'right': -200}  # Tracks the current height of the rods

# Colors for the disks (10 distinct colors)
turtle_colors = [
    "red", "green", "blue", "yellow", "purple", 
    "orange", "pink", "brown", "cyan", "magenta"
]

# Create a turtle for the rods
rod_turtle = turtle.Turtle()
rod_turtle.speed(0)
rod_turtle.hideturtle()

# Function to draw the rods
def draw_rods():
    rod_turtle.penup()
    rod_turtle.goto(-250, -200)
    rod_turtle.pendown()
    rod_turtle.goto(-250, 100)  # Left rod

    rod_turtle.penup()
    rod_turtle.goto(0, -200)
    rod_turtle.pendown()
    rod_turtle.goto(0, 100)  # Middle rod

    rod_turtle.penup()
    rod_turtle.goto(250, -200)
    rod_turtle.pendown()
    rod_turtle.goto(250, 100)  # Right rod

# Create a disk turtle
def create_disk(disk_number, size, color):
    disk = turtle.Turtle()
    disk.shape("square")
    disk.shapesize(stretch_wid=1, stretch_len=size)  # Stretch to make it rectangular
    disk.color(color)
    disk.penup()
    disk.goto(-250, rod_heights['left'])  # Place disk at the left rod's initial height
    rod_heights['left'] += 20  # Increment the rod height for the next disk
    disks.append(disk)
    rods['left'].append(disk)

# Move a disk
def move_disk(disk, start_rod, end_rod):
    # Move disk horizontally and adjust vertical height based on current stack height
    disk.setheading(0)  # Reset heading
    new_y = rod_heights[end_rod]
    
    # Move disk to new rod's vertical position
    disk.goto({
        'left': -250,
        'middle': 0,
        'right': 250
    }[end_rod], new_y)
    
    # Update the rod's height and the rods list
    rod_heights[end_rod] += 20
    rod_heights[start_rod] -= 20
    rods[start_rod].remove(disk)
    rods[end_rod].append(disk)

    time.sleep(0.5)  # Delay to animate the movement

# Recursive function to solve the Tower of Hanoi
def tower_of_hanoi(n, start_rod, end_rod, temp_rod):
    if n == 1:
        move_disk(rods[start_rod][-1], start_rod, end_rod)
        return
    tower_of_hanoi(n-1, start_rod, temp_rod, end_rod)
    move_disk(rods[start_rod][-1], start_rod, end_rod)
    tower_of_hanoi(n-1, temp_rod, end_rod, start_rod)

# Main program
def main():
    # Draw the rods
    draw_rods()

    # Number of disks
    num_disks = 10

    # Create the disks with distinct colors
    for i in range(num_disks):
        create_disk(i, num_disks - i, turtle_colors[i])

    # Solve the Tower of Hanoi problem with animation
    tower_of_hanoi(num_disks, 'left', 'right', 'middle')

    # Wait for a click to close the window
    screen.exitonclick()

if __name__ == "__main__":
    main()
