with open("input.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0

guard_map = {}
guard = (0, 0)
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        guard_map[(i, j)] = char
        if char == "^":
            guard = (i, j)
            guard_map[(i, j)] = "."
og_guard = guard

cur_dir = "UP"
visited = set()
while True:
    visited.add(guard)
    if cur_dir == "UP":
        if (guard[0] - 1, guard[1]) not in guard_map:
            break
        if guard_map[(guard[0] - 1, guard[1])] == ".":
            guard = (guard[0] - 1, guard[1])
        else:
            cur_dir = "RIGHT"
    elif cur_dir == "RIGHT":
        if (guard[0], guard[1] + 1) not in guard_map:
            break
        if guard_map[(guard[0], guard[1] + 1)] == ".":
            guard = (guard[0], guard[1] + 1)
        else:
            cur_dir = "DOWN"
    elif cur_dir == "DOWN":
        if (guard[0] + 1, guard[1]) not in guard_map:
            break
        if guard_map[(guard[0] + 1, guard[1])] == ".":
            guard = (guard[0] + 1, guard[1])
        else:
            cur_dir = "LEFT"
    elif cur_dir == "LEFT":
        if (guard[0], guard[1] - 1) not in guard_map:
            break
        if guard_map[(guard[0], guard[1] - 1)] == ".":
            guard = (guard[0], guard[1] - 1)
        else:
            cur_dir = "UP"
answer1 = len(visited)
print("Answer 1:", answer1)

for obstacle in visited:
    guard_map[(obstacle[0], obstacle[1])] = "#"
    guard = og_guard
    cur_dir = "UP"
    loop = True
    for _ in range(len(visited) * 2):
        if cur_dir == "UP":
            if (guard[0] - 1, guard[1]) not in guard_map:
                loop = False
                break
            if guard_map[(guard[0] - 1, guard[1])] == ".":
                guard = (guard[0] - 1, guard[1])
            else:
                cur_dir = "RIGHT"
        elif cur_dir == "RIGHT":
            if (guard[0], guard[1] + 1) not in guard_map:
                loop = False
                break
            if guard_map[(guard[0], guard[1] + 1)] == ".":
                guard = (guard[0], guard[1] + 1)
            else:
                cur_dir = "DOWN"
        elif cur_dir == "DOWN":
            if (guard[0] + 1, guard[1]) not in guard_map:
                loop = False
                break
            if guard_map[(guard[0] + 1, guard[1])] == ".":
                guard = (guard[0] + 1, guard[1])
            else:
                cur_dir = "LEFT"
        elif cur_dir == "LEFT":
            if (guard[0], guard[1] - 1) not in guard_map:
                loop = False
                break
            if guard_map[(guard[0], guard[1] - 1)] == ".":
                guard = (guard[0], guard[1] - 1)
            else:
                cur_dir = "UP"
    if loop:
        answer2 += 1
    guard_map[(obstacle[0], obstacle[1])] = "."
print("Answer 2:", answer2)
