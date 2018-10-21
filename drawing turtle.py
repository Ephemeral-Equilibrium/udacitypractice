import turtle

window = turtle.Screen()
window.bgcolor("white")

def draw_square(some_turtle):
    for i in range (1,45):
        some_turtle.forward(100)
        some_turtle.right(40.9)
        some_turtle.forward(100)
        some_turtle.right(140)
        some_turtle.forward(100)
        some_turtle.right(40)
        some_turtle.forward(100)

    some_turtle.right(90)
    some_turtle.forward(300)
    some_turtle.right(180)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    bread = turtle.Turtle()
    bread.shape("arrow")
    bread.color("purple")
    bread.speed(1000000)
    draw_square(bread)
    
    window.exitonclick()

draw_art()
