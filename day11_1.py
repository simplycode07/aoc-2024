with open("input.txt") as file:
    raw_data = [i for i in file.read().split()]


def blink():
    new_raw_data = []
    for i, stone in enumerate(raw_data):
        if stone == '0':
            new_raw_data.append('1')

        elif not len(stone) % 2:
            new_raw_data.append(stone[:len(stone)//2])
            new_raw_data.append(str(int(stone[len(stone)//2:])))

        else:
            new_raw_data.append(str(int(stone) * 2024))

    return new_raw_data

print(raw_data)

for i in range(25):
    raw_data = blink()
    print(len(raw_data))

