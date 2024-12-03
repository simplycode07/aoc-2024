import re

with open("input.txt") as file:
    raw_data = file.read()


pattern = r"(do|don't)\(\)|mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, raw_data)

result = 0
do = True
for found in matches:
    brr, num1, num2 = found
    if brr == "do":
        do = True
    elif brr == "don't":
        do = False
    else:
        if do: result += int(num1) * int(num2)
        print(result)

print(result)
