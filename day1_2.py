with open("input.txt") as file:
    tests = file.readlines()

left_list = [int(i.split()[0]) for i in tests]
right_list = [int(i.split()[1]) for i in tests]


similarity_score = 0

for location_id in left_list:
    similarity_score += location_id * right_list.count(location_id)

print(similarity_score)

