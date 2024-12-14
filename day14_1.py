import re

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
final_robots = []

for start_x, start_y, vel_x, vel_y in robots:
    final_robots.append([(start_x + vel_x * 100) % width, (start_y + vel_y * 100) % height])


quads = [0, 0, 0, 0]

center_x = width // 2
center_y = height // 2

# Loop through the final positions of the robots
for x, y in final_robots:
    # Ignore robots in the middle of the grid
    if x == center_x and y == center_y:
        continue
    
    # Assign robots to quadrants
    if x < center_x and y < center_y:
        quads[0] += 1  # Top-left (Q1)
    elif x > center_x and y < center_y:
        quads[1] += 1  # Top-right (Q2)
    elif x < center_x and y > center_y:
        quads[2] += 1  # Bottom-left (Q3)
    elif x > center_x and y > center_y:
        quads[3] += 1  # Bottom-right (Q4)

print(quads)

product = 1
for num in quads:
    product *= num
print(product)
