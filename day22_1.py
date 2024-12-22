with open("input.txt") as file:
    raw_data = [int(line.rstrip()) for line in file]

def mix(num1, num2):
    return num1 ^ num2

def prune(num):
    return num % 16777216

res = 0
for num in raw_data:
    secret_num = num
    for i in range(2000):
        secret_num = prune(mix(secret_num, secret_num*64))
        secret_num = prune(mix(secret_num, int(secret_num / 32)))
        secret_num = prune(mix(secret_num, secret_num * 2048))
    
    res += secret_num
    print(secret_num)

print(res)

print("------------------")
