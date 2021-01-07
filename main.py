from turtle import Turtle, Screen
franklin = Turtle()
franklin.color("green")
franklin.shape("turtle")

#making square
# franklin.forward(45)
# franklin.right(90)
# franklin.forward(45)
# franklin.right(90)
# franklin.forward(45)
# franklin.right(90)
# franklin.forward(45)

#Drawing dashed line

for i in range(50):
    franklin.forward(10)
    franklin.penup()
    franklin.forward(10)
    franklin.pendown()
    franklin.forward(10)
    franklin.penup()
    franklin.forward(10)
    # franklin.penup()
    # franklin.pendown()
    # franklin.penup()







screen = Screen()
screen.exitonclick()