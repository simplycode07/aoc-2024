with open("input.txt") as file:
    tests = file.readlines()

left_list = [int(i.split()[0]) for i in tests]
right_list = [int(i.split()[1]) for i in tests]


distance = 0
for i in range(len(tests)):
    left_min = min(left_list)
    right_min = min(right_list)
    
    distance += abs(left_min - right_min)
    
    left_list.remove(left_min)
    right_list.remove(right_min)

print(distance)

