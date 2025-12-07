topmap = []

with open("puzzle_input_1.txt", "r") as f:
    for line in f:
        word = []
        for w in line.strip():
            word.append(w)
        topmap.append(word)

cols = len(topmap[0])
rows = len(topmap)

for r in range(rows):
    for c in range(cols):
        if topmap[r][c] == "S":
            topmap[r][c] = "|"

count = 0

for r in range(rows - 1):
    for c in range(cols):
        if topmap[r][c] == "|":
            if topmap[r + 1][c] == ".":
                topmap[r + 1][c] = "|"
            if topmap[r + 1][c] == "^":
                topmap[r + 1][c + 1] = "|"
                topmap[r + 1][c - 1] = "|"
                count += 1

for t in topmap:
    print(*t)

print(count)
