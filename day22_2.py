with open("input.txt") as file:
    raw_data = [int(line.rstrip()) for line in file]

def mix(num1, num2):
    return num1 ^ num2

def prune(num):
    return num % 16777216

res = 0
total = {}
for num in raw_data:
    secret_num = num
    pattern = []
    last = secret_num % 10
    for i in range(2000):
        secret_num = prune(mix(secret_num, secret_num*64))
        secret_num = prune(mix(secret_num, int(secret_num / 32)))
        secret_num = prune(mix(secret_num, secret_num * 2048))
        temp = secret_num % 10
        pattern.append((temp - last, temp))
        last = temp

    seen = set()
    for i in range(len(pattern)-4):
        pat = tuple(x[0] for x in pattern[i:i+4])
        val = pattern[i+3][1]
        if pat not in seen:
            seen.add(pat)
            if pat not in total:
                total[pat] = val
            else:
                total[pat] += val
    

print(max(total.values()))

print("------------------")
