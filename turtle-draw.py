import turtle

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
    my_points = [[x*2 for x in y] for y in my_points]
    print(my_points)
    sierpinski(my_points, 6, my_turtle)
    my_win.exitonclick()

main()