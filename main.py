from turtle import Turtle, Screen
import random



franklin = Turtle()



#creating random color

# def random_color(n1, n2, n3):
#     r = random.randint(n1, 255)
#     g = random.randint(n2, 255)
#     b = random.randint(n3, 255)
#     rgb = (r, g, b)
#     return rgb
# print(random_color(148, 207, 223))


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

# for i in range(50):
#     franklin.forward(10)
#     franklin.penup()
#     franklin.forward(10)
#     franklin.pendown()
#     franklin.forward(10)
#     franklin.penup()
#     franklin.forward(10)
  

#Making shapes
#triangle
# franklin.forward(120)
# franklin.right(120)
# franklin.forward(120)
# franklin.right(120)
# franklin.forward(120)
# #square
# franklin.forward(45)
# franklin.right(90)
# franklin.forward(45)
# franklin.right(90)
# franklin.forward(45)
# franklin.right(90)
# franklin.forward(45)
# #pentagon
# franklin.forward(72)
# franklin.right(72)
# franklin.forward(72)
# franklin.right(72)
# franklin.forward(72)
# franklin.right(72)
# franklin.forward(72)

# #hexagon
# franklin.forward(60)
# franklin.right(60)
# franklin.forward(60)
# franklin.right(60)
# franklin.forward(60)
# franklin.right(60)
# franklin.forward(60)
# franklin.right(60)
# franklin.forward(60)
# franklin.right(60)
# franklin.right(60)
# franklin.forward(60)
# franklin.right(60)




#Random walk

# franklin.pensize(10)
# colors = ["AliceBlue", "CadetBlue", "DarkSeaGreen", "green", "black", "cornsilk1", "DarkOrange", "aquamarine4"]



# movement = [0, 90, 180, 270]

# for _ in range(200):
#     # franklin.color(random.choice(colors)) this works but for the next challenge we will try doing this with tuples
#     franklin.forward(30)
#     franklin.setheading(random.choice(movement))






#Making shapes but using a function - what angela did
# Since the number of sides wont be the same for all the shapes we will use a function 
# def draw_shape (num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         franklin.forward(100)
#         franklin.right(angle)
        # franklin.forward(random.choice(colors))

  # draw_shape(3)
    # draw_shape(4)
    # draw_shape(5)



# for moves in movement:
#     random.choice(colors)        
#     random.choice(movement)
    # random.choice(movement)
    # random.choice(movement)
    # random.choice(movement)

# def move(number):
#     franklin.forward(number)
#     franklin.left(number)
#     franklin.right(number)
#     franklin.backward(number)
#     franklin.circle(number)

# move(30)

#Draw a circle 


#It works did it by myself -Made spirograph
for _ in range(45):
    franklin.circle(50) #100
    franklin.forward(10)
    franklin.right(10)

    # for _ in range(45):
    #     franklin.circle(50) #100
    #     franklin.forward(10)
    #     franklin.right(10)
   




























screen = Screen()
screen.exitonclick()

# random.choice()



