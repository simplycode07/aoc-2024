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

program_match = re.search(program_pattern, raw_data)
program = list(map(int, program_match.group(1).split(',')))


# 108,107,552,267,785 -> 6
# 108,107,574,679,062 -> 10
registers = {"A":108_107_574_679_062, "B":0, "C":0}
# print(registers)
# print(program)

def combo_operand(mod_registers, operand):
    # if operand == 7: print("operand was 7")
    if operand <= 3:
        return operand
    # print("on reg ", operand, operand-4, list(registers.values())[operand-4])
    return list(mod_registers.values())[operand-4]

def execute_program(mod_registers):
    output_buffer = []
    i = 0
    while i < len(program):
        opcode = program[i]
        operand = program[i+1]
        # print(opcode, operand)
        i += 2
        
        # print(opcode, operand)
        if opcode == 0:
            num = mod_registers["A"]
            den = 2 ** combo_operand(mod_registers, operand)
            
            res = num / den
            mod_registers["A"] = int(res)

        elif opcode == 1:
            mod_registers["B"] = mod_registers["B"] ^ operand

        elif opcode == 2:
            mod_registers["B"] = combo_operand(mod_registers, operand) % 8

        elif opcode == 3:
            if mod_registers["A"] != 0:
                i = operand

        elif opcode == 4:
            mod_registers["B"] = mod_registers["C"] ^ mod_registers["B"]

        elif opcode == 5:
            output_buffer.append(combo_operand(mod_registers, operand) % 8)

        elif opcode == 6:
            num = mod_registers["A"]
            den = 2 ** combo_operand(mod_registers, operand)
            
            res = num / den
            mod_registers["B"] = int(res)

        elif opcode == 7:
            num = mod_registers["A"]
            den = 2 ** combo_operand(mod_registers, operand)
            
            res = num / den
            mod_registers["C"] = int(res)
    
    return output_buffer


while 1:
    i = 0
    output = execute_program(registers.copy())
    if output == program:
        print(registers["A"])
        quit()

    elif output[-13:] == program[-13:]:
        registers["A"] += 1
        print(f"{registers["A"]:,}, {output}")

    elif output[-10:] == program[-10:]:
        registers["A"] += 100
        print(f"{registers["A"]:,}, {output}")

    elif output[-6:] == program[-6:]:
        registers["A"] += 100_000
        print(f"{registers["A"]:,}, {output}")

    elif output[-3:] == program[-3:]:
        registers["A"] += 1_000_000
        print(f"{registers["A"]:,}, {output}")

    elif output[-2:] == program[-2:]:
        registers["A"] += 10_000_000
        print(f"{registers["A"]:,}, {output}")
    else:
        registers["A"] += 1_000_000_000
        print(f"{registers["A"]:,}, {output}")

