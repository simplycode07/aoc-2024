import re
import numpy as np
import cv2

with open("input.txt") as file:
    data = file.read()
width = 101
height = 103

# width = 11
# height = 7


pattern = r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)"

matches = re.findall(pattern, data)

# Convert the matched groups into a list of tuples of integers
robots = [[int(x[0]), int(x[1]), int(x[2]), int(x[3])] for x in matches]

def update_robot(t):
    final_robots = []
    for start_x, start_y, vel_x, vel_y in robots:
        final_robots.append([(start_x + vel_x * t) % width, (start_y + vel_y * t) % height])
    grid = np.zeros((height, width))

    seen = set()
    for x, y in final_robots:
        if (x,y) in seen:
            return False

        grid[y,x] = 255
        seen.add((x, y))

    # if len(seen) == len(robots):
    # return len(seen) == len(robots)
    cv2.imwrite(f"{t}.png", grid)


for t in range(100000):
    worked = update_robot(t)
    print(worked, t)

