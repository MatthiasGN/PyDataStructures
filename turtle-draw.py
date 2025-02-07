import turtle

def draw_line(my_turtle, line_len):
    if line_len > 2:
        my_turtle.forward(line_len)
        my_turtle.right(121)
        draw_line(my_turtle, line_len-2)

def draw_line_alt_colours(my_turtle, line_len, colour_idx):
    colour_map = ["red", "blue"]
    if line_len > 2:
        my_turtle.color(colour_map[colour_idx])
        my_turtle.forward(line_len)
        my_turtle.right(121)
        draw_line_alt_colours(my_turtle, line_len-2, 1-colour_idx)

def draw_line_triangle_colours(my_turtle, line_len, ctr):
    colour_map = ["red", "blue"]
    # colour_map = ["red", "blue", "gold"]
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
        draw_line_triangle_colours(my_turtle, line_len-2, ctr)

t = turtle.Turtle()
my_win = turtle.Screen()
t.speed(0)
t.up()
t.backward(200)
t.left(90)
t.backward(300)
t.down()


# Simple draw line
# draw_line(t, 600)

# Alternating colours / pen size
t.color("red")
t.pensize(6) # PLAY AROUND WITH THIS!!

# draw_line_alt_colours(t, 600, 0)
draw_line_triangle_colours(t, 600, 0)

t.up()
t.backward(500)
my_win.exitonclick()