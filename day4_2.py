with open("input.txt") as file:
    data = file.readlines()


def find_cross(board, x, y):
    diagonal1 = [(1, 1), (-1, -1)]
    diagonal2 = [(-1, 1), (1, -1)]
    
    board_diagonal1 = ""
    for i,j in diagonal1:
        if 0 <= y - j < len(board) and 0 <= x - i < len(board[0]):
            # print(f"at: {x - i},{y - j}")
            board_diagonal1 += board[y - j][x - i]

    board_diagonal2 = ""
    for i,j in diagonal2:
        if 0 <= y - j < len(board) and 0 <= x - i < len(board[0]):
            # print(f"at: {x - i},{y - j}")
            board_diagonal2 += board[y - j][x - i]
    
    # print(board_diagonal1, board_diagonal2)
    if (board_diagonal1 == board_diagonal2 or board_diagonal1 == board_diagonal2[::-1]) and board_diagonal1 in ["MS", "SM"]:
        return 1

    return 0

res = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "A":
            res += find_cross(data, x, y)

print(res)

# find_cross(data, 2, 1)
