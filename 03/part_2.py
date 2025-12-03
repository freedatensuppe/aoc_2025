with open("puzzle_input_1.txt", "r") as f:
    nums = [line.strip() for line in f.read().splitlines()]

highs = []

for num in nums:
    numlist = list(map(int, list(num)))
    while len(numlist) > 12:
        cands = []
        for i, _ in enumerate(numlist):
            cand = numlist[:i] + numlist[(i + 1) :]
            cands.append(int("".join(map(str, cand))))
        highest = max(cands)
        numlist = list(map(int, str(highest)))

    high = int("".join(map(str, numlist)))
    highs.append(high)


print(highs)
print(sum(highs))
