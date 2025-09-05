## Hirst Painting

import random
import turtle as t
import colorgram


# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(rgb_colors)


color_list = [
    (219, 173, 124), (159, 180, 190), (134, 73, 53), (49, 102, 153),
    (118, 82, 93), (179, 140, 150), (41, 46, 65), (162, 104, 151),
    (126, 173, 114), (83, 96, 183), (67, 9, 27), (81, 133, 107),
    (231, 188, 138), (52, 62, 79), (195, 90, 72), (116, 43, 58),
    (60, 41, 28), (92, 144, 117), (70, 67, 52), (182, 187, 207),
    (211, 181, 189), (102, 51, 38), (174, 199, 203), (181, 201, 180),
    (210, 184, 180), (41, 73, 82)
]


tim = t.Turtle()
t.colormode(255)
# tim.speed("fastest")
tim.up()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

x_pos = tim.pos()[0]
y_pos = tim.pos()[1]
for row in range(10):
    tim.setpos(x_pos, y_pos + 50*row)
    for _ in range (10):
            tim.begin_fill()
            tim.dot(20, random.choice(color_list))
            tim.end_fill()
            tim.forward(50)

t.mainloop()