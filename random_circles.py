import random
import cv2
import numpy as np

# helpers

def rand_color():
    return tuple(random.uniform(0, 1) for i in range(3))

def rand_radius(max=100):
    return random.randint(0, max)

def rand_thickness(max=5):
    fill = random.choice([True, False])
    return -1 if fill else random.randint(1, max)

# state
img = np.zeros((600, 600, 3))

# functions

def draw_circle(event, x, y, flags, param):
#     print("***************")
#     print("Drawing circle:")
#     print("Event:", event)
#     print("x:", x)
#     print("y:", y)
#     print("flags:", flags)
#     print("param:", param)
    
    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x, y)
        radius = rand_radius()
        color = rand_color()
        print("color:", color)
        thickness = rand_thickness()
        cv2.circle(img, center, radius, color, thickness)

cv2.namedWindow(winname="my_drawing")
cv2.setMouseCallback("my_drawing", draw_circle)

# MAIN

while True:
    cv2.imshow("my_drawing", img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
    