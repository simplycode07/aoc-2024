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
    final_x += 10000000000000
    final_y += 10000000000000

    i_value = (final_x * button_b_y - final_y * button_b_x) / (button_a_x * button_b_y - button_a_y * button_b_x)
    j_value = (final_y * button_a_x - final_x * button_a_y) / (button_a_x * button_b_y - button_a_y * button_b_x)
    if i_value == int(i_value) and j_value == int(j_value):
        return 3 * i_value + j_value
    
    return 0
    # Return the weighted score based on the solution
res = 0
for game in games:
    res += solve(*game)

print(res)


