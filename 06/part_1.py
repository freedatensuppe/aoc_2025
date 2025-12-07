with open("puzzle_input_1.txt", "r") as f:
    input = f.read().strip().split("\n")

nums = [list(map(int, i.split())) for i in input[:-1]]
nums = list(map(list, zip(*nums)))
ops = input[-1].split()

print(nums)
print(ops)

results = []

for i, num in enumerate(nums):
    op = ops[i]
    res = 1 if op == "*" else 0
    for n in num:
        res = eval("res" + op + "n")
    results.append(res)

print(results)
print(sum(results))
