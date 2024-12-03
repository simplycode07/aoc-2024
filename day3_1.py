import re

with open("input.txt") as file:
    raw_data = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, raw_data)

result = 0
for found in matches:
    num1, num2 = found
    result += int(num1) * int(num2)

print(result)
