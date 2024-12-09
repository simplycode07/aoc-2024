with open("input.txt") as file:
    raw_data = file.read()

disk = []
free_space = []
i = 0
while i < len(raw_data) // 2:
    for j in range(int(raw_data[2*i])):
        disk.append(i)

    if raw_data[2*i+1] != "\n":
        for j in range(int(raw_data[2*i+1])):
            free_space.append(len(disk))
            disk.append(-1)

    i += 1

# print(disk)
# print(free_space)

def swap(i1, i2):
    temp = disk[i1]
    disk[i1] = disk[i2]
    disk[i2] = temp

def calc_checksum(disk):
    visited = set()
    checksum = 0
    for i, file in enumerate(disk):
        if file == -1:
            continue
        if file in visited:
            continue
        
        checksum += i * file
        
    return checksum

swap_counter = 0
i = len(disk) - 1
while i > len(disk) - 1 - len(free_space) and swap_counter < len(free_space):
    print(i)
    if disk[i] != -1:
        swap(i, free_space[swap_counter])
        swap_counter += 1
    i -= 1

# print(disk)

print(calc_checksum(disk))
