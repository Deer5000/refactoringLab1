# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math
def distance_between():
    circle1X = 4
    circle1Y = 4.25

    circle2X = 53
    circle2Y = -5.35
    # Calculate the distance between the two circle
    distance = math.sqrt((circle1X-circle2X)**2 + (circle1Y - circle2Y)**2)
    print('distance', distance)
# *** somewhere else in your program ***
def calculate_length():
    xOfPointA = -36
    yOfPointA = 97

    xOfPointB = .34
    yOfPointB = .91
    # calcualte the length of vector AB vector which is a vector between A and B points.
    length = math.sqrt((xOfPointA-xOfPointB)*(xOfPointA-xOfPointB) + (yOfPointA-yOfPointB)*(yOfPointA-yOfPointB))
    print('length', length)

distance_between()
calculate_length()