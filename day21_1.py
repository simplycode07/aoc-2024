with open("sample.txt") as file:
    raw_data = [line.rstrip() for line in file]

keypad = [["7", "8", "9"],
          ["4", "5", "6"],
          ["1", "2", "3"],
          [-1, "0", "A"]]

# keypad = [-1, 0, "A", 1, 2, 3, 4, 5, 6, 7, 8, 9]

#               up       left    down    right
# directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

#               up       left    down    right
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

dir_keypad = [[-1, "^", "A"],
              ["<", "v", ">"]]

def get_pos(grid, element):
    for i, row in enumerate(grid):
        for j, ele in enumerate(row):
            if ele == element:
                return (i, j)
    return (-1, -1)

final_robot = [2, 3]
def get_sequence(grid, pos, code):
    pos = pos
    seq = []
    for key in code:
        final_pos = get_pos(grid, key)
        # print(f"")
        
        diff_r = final_pos[0] - pos[0]
        diff_c = final_pos[1] - pos[1]
        pos = list(final_pos)
        print(f"final_pos: {final_pos}, r:{diff_r}, c:{diff_c}, key: {key}")
        
        curr_seq = ""
        if diff_c > 0:
            curr_seq += ">"*diff_c
        elif diff_c < 0:
            curr_seq += "<"*-diff_c
        
        if diff_r > 0:
            curr_seq += "v"*diff_r
        elif diff_r < 0:
            curr_seq += "^"*-diff_r

        if curr_seq != "":
            seq.append(curr_seq)
        seq.append("A")

    return seq

# res = 0
# for code in raw_data:
#     final_seq = get_sequence(keypad, [3, 2], code)
#     r1 = get_sequence(dir_keypad, [0, 2], [char for s in final_seq for char in s])
#     r2 = get_sequence(dir_keypad, [0, 2], [char for s in r1 for char in s])
#
#     res += int(code[:3]) * len("".join(r2))
#     print(int(code[:3]), len("".join(r2)))
#
# print(res)
final_seq = get_sequence(keypad, [3, 2], "456A")
print("---------")
r1 = get_sequence(dir_keypad, [0, 2], [char for s in final_seq for char in s])
print("---------")
r2 = get_sequence(dir_keypad, [0, 2], [char for s in r1 for char in s])
print("---------")


print("".join(final_seq))
print("".join(r1))
print("".join(r2))
print(len("".join(r2)))
