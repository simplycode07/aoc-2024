from itertools import product

with open("input.txt") as file:
    raw_data = file.readlines()

equations = []

for data in raw_data:
    res = int(data.split(":")[0])
    nums = [int(num) for num in data.split(":")[1].split()]

    equations.append((res, nums))

print(equations)

def evaluate_exp(nums, operations):
    res = nums[0]
    for i in range(1, len(nums)):
        if operations[i-1] == "+":
            print("add:", res, nums[i], operations[i-1])
            res += nums[i]
        else:
            print("mul:", res, nums[i], operations[i-1])
            res *= nums[i]

    return res

result = 0
operations = ["+", "*"]

for eqn in equations:
    res, nums = eqn
    # print(res, nums)
    for ops in product(operations, repeat=len(nums) - 1):
        print(ops)
        if evaluate_exp(nums, ops) == res:
            result += res
            break
        # else:
        #     print(evaluate_exp(nums, ops), res)

print(result)
