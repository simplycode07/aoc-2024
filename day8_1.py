with open("input.txt") as file:
    raw_data = file.readlines()

rows = len(raw_data)
cols = len(raw_data[0].strip())

antennas = {}
for y, data in enumerate(raw_data):
    for x, grid in enumerate(data.strip()):
        if grid == ".":
            continue

        if antennas.get(grid):
            antennas[grid].append((x, y))
        else:
            antennas[grid] = [(x, y)]

# print(rows, cols)
# print(antennas)

antinodes = set()

def antinode(antenna1, antenna2):
    x1, y1 = antenna1
    x2, y2 = antenna2
        
    possible_antinode = (x2 + (x2 - x1), y2 + (y2 - y1))

    if 0 <= possible_antinode[0] < cols and 0 <= possible_antinode[1] < rows:
        antinodes.add(possible_antinode)

for same_freq_ants in antennas.values():
    for i in range(len(same_freq_ants)):
        for j in range(i):
            antinode(same_freq_ants[i], same_freq_ants[j])
            antinode(same_freq_ants[j], same_freq_ants[i])

    
print(len(antinodes))
