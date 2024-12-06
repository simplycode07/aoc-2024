with open("input.txt") as file:
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

def detect_loop(x, y, obs_dict, pos, curr_dir):
    obs_dict[f"{x};{y}"] = True

    turns_taken = {}
    turns_taken[f"{pos[0]};{pos[1]};{curr_dir}"] = True

    while 0 < pos[0] < len(map[0]) and 0 < pos[1] < len(map):
        direction = directions[curr_dir]
        next_pos = [pos[0] + direction[0], pos[1] + direction[1]]

        if obs_dict.get(f"{next_pos[0]};{next_pos[1]}"):
            curr_dir += 1
            curr_dir %= len(directions)
            if turns_taken.get(f"{pos[0]};{pos[1]};{curr_dir}"):
                print("loop found at", pos, curr_dir)
                return True
            else:
                turns_taken[f"{pos[0]};{pos[1]};{curr_dir}"] = True

        else:
            pos = next_pos

    return False

loops = 0
for x in range(len(map[0])):
    for y in range(len(map)):
        if not obs_dict.get(f"{x};{y}"):
            if detect_loop(x, y, obs_dict.copy(), pos, curr_dir):
                print(x, y)
                loops += 1

print(detect_loop(3, 6, obs_dict, pos, curr_dir))

print(loops)
