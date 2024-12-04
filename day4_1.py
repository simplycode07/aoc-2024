with open("input.txt") as file:
    raw_data = file.readlines()

board = []
for data in raw_data:
    board.append(data.strip())

word = "XMAS"

def find_xmas(board, x, y, change):
    x += change[0]
    y += change[1]
    counter = 1
    while x < len(board[0]) and y < len(board) and counter < len(word) and x >= 0 and y >= 0:
        if board[y][x] == word[counter]:
            counter += 1
        else:
            break

        x += change[0]
        y += change[1]

    return 1 if counter == len(word) else 0

allowed_changes = [(0,1), (0,-1),
                   (1,0), (-1,0),
                   (-1,-1), (1,-1), (1,1), (-1,1)]
num_xmas = 0
for y in range(len(board)):
    for x in range(len(board[0])):
        if board[y][x] == "X":
            for change in allowed_changes:
                num_xmas += find_xmas(board, x, y, change)

print(num_xmas)




