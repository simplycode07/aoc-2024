import re
import pygame
from time import sleep

pygame.init()

with open("input.txt") as file:
    data = file.read()
width = 101
height = 103
block_size = 8

pattern = r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)"
matches = re.findall(pattern, data)
robots = [[int(x[0]), int(x[1]), int(x[2]), int(x[3])] for x in matches]


display = pygame.display.set_mode((width*block_size, height*block_size))


# def update_robot(t):
#     final_robots = []
#     for start_x, start_y, vel_x, vel_y in robots:
#         final_robots.append([(start_x + vel_x * t) % width, (start_y + vel_y * t) % height])
#
#     seen = set()
#     for x, y in final_robots:
#         if (x,y) in seen:
#             return False
#
#         seen.add((x, y))
#
# for t in range(100000):
#     worked = update_robot(t)
#     print(worked, t)

running = True
count = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if not count % 100:
        for robot in robots:
            rect = pygame.Rect(robot[0] * block_size, robot[1] * block_size, block_size, block_size)
            pygame.draw.rect(display, (13, 210, 240), rect)
                
            robot[0] += robot[2]
            robot[1] += robot[3]

            robot[0] %= width
            robot[1] %= height
        pygame.display.update()
        display.fill((30, 30, 20))

    count += 1
    if not count % (6588 * 100):
        input()
    # sleep(0.1)



