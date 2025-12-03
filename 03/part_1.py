with open("puzzle_input_1.txt", "r") as f:
    nums = [line.strip() for line in f.read().splitlines()]

highs = []

for num in nums:
    numlist = list(map(int, list(num)))
    first = max(numlist)
    ind = numlist.index(first)
    if ind != len(num) - 1:
        second = max(numlist[(ind + 1) :])
        high = 10 * first + second
        highs.append(high)
    else:
        first = max(numlist[:-1])
        ind = numlist.index(first)
        second = max(numlist[(ind + 1) :])
        high = 10 * first + second
        highs.append(high)

print(sum(highs))
