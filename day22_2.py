with open("input.txt") as file:
    raw_data = [int(line.rstrip()) for line in file]

total = {}
for num in raw_data:
    secret_num = num
    pattern = []
    last = secret_num % 10
    for _ in range(2000):
        secret_num = ((secret_num << 6) ^ secret_num) % 16777216
        secret_num = ((secret_num // 32) ^ secret_num) % 16777216
        secret_num = ((secret_num << 11) ^ secret_num) % 16777216
        temp = secret_num % 10
        pattern.append((temp - last, temp))
        last = temp

    seen = set()
    for i in range(len(pattern)-4):
        pat = tuple(x[0] for x in pattern[i:i+4])
        val = pattern[i+3][1]
        if pat not in seen:
            seen.add(pat)
            if not total.get(pat):
                total[pat] = val
            else:
                total[pat] += val
    

print(max(total.values()))

print("------------------")
