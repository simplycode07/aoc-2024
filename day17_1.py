import re

with open("input.txt") as file:
    raw_data = file.read()
    # raw_regs, instructions = file.read().split("\n\n")
    #
    # regs = raw_regs.split(":")
    #
    # instructions = instructions.strip().split(",")
    # instructions[0] = instructions[0].split(":")[1].strip()


register_pattern = r"Register ([A-C]): (\d+)"
program_pattern = r"Program: ([\d,]+)"

registers = {}
for match in re.findall(register_pattern, raw_data):
    label, value = match
    registers[label] = int(value)

program_match = re.search(program_pattern, raw_data)
program = list(map(int, program_match.group(1).split(',')))

print(registers)
print(program)

def combo_operand(operand):
    # if operand == 7: print("operand was 7")
    if operand <= 3:
        return operand
    print("on reg ", operand, operand-4, list(registers.values())[operand-4])
    return list(registers.values())[operand-4]

# for i in range(7):
#     print(combo_operand(i))
output_buffer = []
i = 0
while i < len(program):
    opcode = program[i]
    operand = program[i+1]
    # print(opcode, operand)
    i += 2
    
    # print(opcode, operand)
    if opcode == 0:
        num = registers["A"]
        den = 2 ** combo_operand(operand)
        
        res = num / den
        registers["A"] = int(res)

    elif opcode == 1:
        registers["B"] = registers["B"] ^ operand

    elif opcode == 2:
        registers["B"] = combo_operand(operand) % 8

    elif opcode == 3:
        if registers["A"] != 0:
            i = operand

    elif opcode == 4:
        registers["B"] = registers["C"] ^ registers["B"]

    elif opcode == 5:
        output_buffer.append(combo_operand(operand) % 8)

    elif opcode == 6:
        num = registers["A"]
        den = 2 ** combo_operand(operand)
        
        res = num / den
        registers["B"] = int(res)

    elif opcode == 7:
        num = registers["A"]
        den = 2 ** combo_operand(operand)
        
        res = num / den
        registers["C"] = int(res)


for i in output_buffer:
    print(i, end=",")

print()
print(registers)
