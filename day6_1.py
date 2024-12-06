with open("sample.txt") as file:
    raw_data = file.readlines()

map = []
for data in raw_data:
    map.append(data.strip())

print(map[0][-1] == "\n")

directions = [[0,-1], [1,0], [0,1], [-1,0]]
curr_dir = 0

pos = []
obs_dict = {}
for y, row in enumerate(map):
    for x, obj in enumerate(row):
        if obj == "^":
            pos = [x, y]
        if obj == "#":
            obs_dict[f"{x};{y}"] = True

print(pos)
visited = set()
while 0 < pos[0] < len(map[0]) and 0 < pos[1] < len(map):
    direction = directions[curr_dir]
    next_pos = [pos[0] + direction[0], pos[1] + direction[1]]

    print(next_pos)
    if obs_dict.get(f"{next_pos[0]};{next_pos[1]}"):
        curr_dir += 1
        curr_dir %= len(directions)

        print("direction changed on", next_pos, curr_dir)
    else:
        visited.add(f"{next_pos[0]};{next_pos[1]}")
        pos = next_pos

print(len(visited))
