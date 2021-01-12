import colorgram
from turtle import Turtle, Screen  




# dir(colorgram)

rgb_colors = []
colors = colorgram.extract("hirst/hirst.jpg", 84)

# print(colors)


#Extracted color tuples from the picture
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)



print(rgb_colors)

colors_list = [(245, 243, 238), (248, 241, 244), (237, 240, 246), (201, 164, 112), (238, 246, 241), (152, 75, 49), (221, 201, 138), (171, 153, 42), (56, 95, 126), (139, 31, 19), (134, 163, 184), (197, 93, 73), (48, 121, 88), (98, 75, 77), (142, 178, 148), (75, 41, 33), (165, 145, 156), (15, 99, 71), (234, 175, 164), (54, 45, 47), (32, 61, 77), (145, 21, 25), (21, 83, 89), (182, 205, 175), (85, 147, 127), (44, 66, 87), (178, 94, 98), (222, 177, 184), (8, 68, 51), (108, 127, 151), (177, 192, 209), 
    (88, 85, 28), (109, 136, 140), (251, 196, 3), (174, 198, 202)]

t = Turtle()

def painting(list_of_colors):
    for colors in list_of_colors:
        t.pencolor(colors)
        t.pensize(20)

    t.forward(50)


painting(colors_list)
# for colors in colors_list:
    




screen = Screen()
screen.exitonclick()