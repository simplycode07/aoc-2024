from enum import unique
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
robots = [[float(x[0]), float(x[1]), int(x[2]), int(x[3])] for x in matches]

display = pygame.display.set_mode((width*block_size, height*block_size))

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

def draw_text(display, text):
    text_surface = my_font.render(text, False, (255, 255, 255))
    display.blit(text_surface, (0, 0))


slowness = 600
running = True
count = 0
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                count += 100
                for robot in robots:
                    robot[0] += 100 * robot[2]
                    robot[1] += 100 * robot[3]

                    robot[0] %= width
                    robot[1] %= height
            if event.key == pygame.K_2:
                count += 10
                for robot in robots:
                    robot[0] += 10 * robot[2]
                    robot[1] += 10 * robot[3]

                    robot[0] %= width
                    robot[1] %= height

            if event.key == pygame.K_p:
                paused = not paused

    if int(count) == 6587:
        paused = True
        
    if not paused:
        display.fill((30, 30, 20))
        for robot in robots:
            robot[0] += (robot[2] / slowness)
            robot[1] += (robot[3] / slowness)

            robot[0] %= width
            robot[1] %= height

            rect = pygame.Rect(robot[0] * block_size, robot[1] * block_size, block_size, block_size)
            pygame.draw.rect(display, (13, 210, 240), rect)


        count += 1/slowness
    draw_text(display, f"at: {count}")
    pygame.display.update()

    sleep(0.001)



