import re
with open("input.txt", 'r') as file:
    content = file.read()
        
pattern = r"(\w+):\s*(\d+)"
matches = re.findall(pattern, content)

wires = {key: bool(int(value)) for key, value in matches}

pattern = r"(\w+)\s+(\w+)\s+(\w+)\s+->\s+(\w+)"
matches = re.findall(pattern, content)
# print(len(matches))

print(wires)

for _ in range(100):
    for match in matches:
        if match[0] in wires and match[2] in wires and match[3] not in wires:
            if match[1] == "AND":
                wires[match[3]] = wires[match[0]] and wires[match[2]]

            if match[1] == "OR":
                wires[match[3]] = wires[match[0]] or wires[match[2]]

            if match[1] == "XOR":
                wires[match[3]] = wires[match[0]] ^ wires[match[2]]


# print(len(wires))


pattern = r"z\d+"

z_keys = sorted([key for key in wires if re.match(pattern, key)])
z_values = {key: int(wires[key]) for key in z_keys}

binary_number = ''.join(str(z_values[key]) for key in z_keys)
binary_number = binary_number[::-1]
decimal_number = int(binary_number, 2)

print(z_keys)
print(z_values)

print(binary_number)
print(decimal_number)
