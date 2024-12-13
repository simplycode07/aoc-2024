import re

with open("input.txt") as file:
    raw_data = file.read().split("\n\n")

pattern = r'[+-=]?(\d+)'

games = []
for game in raw_data:
    match = re.findall(pattern, game)
    games.append(list(map(int, match)))
    # for match in re.findall(pattern, game):
        # print(match)

# print(games)


def solve(button_a_x, button_a_y, button_b_x, button_b_y, final_x, final_y):
    for i in range(100):
        for j in range(100):
            if i * button_a_x + j * button_b_x == final_x and i * button_a_y + j * button_b_y == final_y:
                print(f"{i}, {j}")
                return i * 3 + j
    
    return 0

res = 0
for game in games:
    res += solve(*game)

print(res)


