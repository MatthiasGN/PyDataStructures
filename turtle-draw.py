import turtle

def draw_triangle(my_turtle, line_len):
    if line_len > 28:
        my_turtle.forward(line_len)
        my_turtle.right(121)
        draw_triangle(my_turtle, line_len-2)

def draw_triangle_alt_colours(my_turtle, line_len, colour_idx):
    colour_map = ["red", "blue"]
    if line_len > 2:
        my_turtle.color(colour_map[colour_idx])
        my_turtle.forward(line_len)
        my_turtle.right(121)
        draw_triangle_alt_colours(my_turtle, line_len-2, 1-colour_idx)

def draw_triangle_colours(my_turtle, line_len, ctr):
    # colour_map = ["red", "blue"]
    colour_map = ["red", "blue", "gold"]
    # colour_map = ["red", "darkorange", "gold", "green", "blue", "purple"]
    if line_len > 2:
        ctr += 1
        if ctr % 3 == 0:
            new_index = colour_map.index(my_turtle.color()[0]) + 1
            if new_index > len(colour_map) - 1:
                new_index = 0
            my_turtle.color(colour_map[new_index])
        my_turtle.forward(line_len)
        my_turtle.right(121)
        draw_triangle_colours(my_turtle, line_len-2, ctr)

t = turtle.Turtle()
my_win = turtle.Screen()
t.speed(0)
t.up()

# TRIANGLES
# t.backward(200)
# t.left(90)
# t.backward(300)
# t.down()
# draw_triangle(t, 600)

# Alternating colours / pen size
# t.color("red")
# t.pensize(6) # PLAY AROUND WITH THIS!!
# draw_triangle_alt_colours(t, 600, 0)
# draw_triangle_colours(t, 600, 0)

# Okay, how about squares?
def draw_square(my_turtle, line_len):
    if line_len > 2:
        my_turtle.forward(line_len)
        my_turtle.right(91)
        draw_square(my_turtle, line_len-2)

def draw_square_colours(my_turtle, line_len, ctr):
    colour_map = ["red", "blue"]
    # colour_map = ["red", "blue", "gold"]
    # colour_map = ["red", "darkorange", "gold", "green", "blue", "purple"]
    if line_len > 2:
        ctr += 1
        if ctr % 4 == 0:
            new_index = colour_map.index(my_turtle.color()[0]) + 1
            if new_index > len(colour_map) - 1:
                new_index = 0
            my_turtle.color(colour_map[new_index])
        my_turtle.forward(line_len)
        my_turtle.right(91)
        draw_square_colours(my_turtle, line_len-2, ctr)

# SQUARES
# t.backward(300)
# t.left(90)
# t.backward(300)
# t.down()
# draw_square(t, 600)

# t.pensize(10)
# t.color("red")
# draw_square_colours(t, 600, 0)


# ... hexagons?

def draw_hexagon(my_turtle, line_len):
    if line_len > 2:
        my_turtle.forward(line_len)
        my_turtle.right(60.5)
        draw_hexagon(my_turtle, line_len-2)

# HEXAGONS
# t.backward(300)
# t.left(90)
# t.backward(150)
# t.down()
# t.pensize(5)
# draw_hexagon(t, 300)


# Let's try something a bit harder... STARS.

def draw_star(my_turtle, line_len, ctr):
    if line_len > 6:
        ctr += 1
        my_turtle.forward(line_len)
        if ctr % 2 == 1:
            my_turtle.left(72.25)
        else:
            my_turtle.right(143.75)
        draw_star(my_turtle, line_len-0.5, ctr)

def draw_star_colours(my_turtle, line_len, ctr):
    # colour_map = ["red", "blue"]
    colour_map = ["red", "blue", "gold"]
    # colour_map = ["red", "darkorange", "gold", "green", "blue"]
    # colour_map = ["red", "darkorange", "gold", "green", "blue", "purple"]
    if line_len > 6:
        ctr += 1
        if ctr % 10 == 0:
            new_index = colour_map.index(my_turtle.color()[0]) + 1
            if new_index > len(colour_map) - 1:
                new_index = 0
            my_turtle.color(colour_map[new_index])
        my_turtle.forward(line_len)
        if ctr % 2 == 1:
            my_turtle.left(72.2)
        else:
            my_turtle.right(143.8)
        draw_star_colours(my_turtle, line_len-0.5, ctr)

# STARS
t.backward(250)
t.left(90)
t.backward(350)
t.right(18)
t.down()
# draw_star(t, 300, 0)

t.pensize(5)
t.color("red")
draw_star_colours(t, 300, 0)

t.up()
t.backward(1200)
my_win.exitonclick()