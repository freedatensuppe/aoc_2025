from copy import deepcopy

topmap = []

with open("puzzle_input_1.txt", "r") as f:
    for line in f:
        word = []
        for w in line.strip():
            word.append(w)
        topmap.append(word)

cols = len(topmap[0])
rows = len(topmap)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, 1), (1, 1), (-1, -1), (1, -1)]


def check_access(topmap, r, c):
    count = 0
    for d in dirs:
        cn = c + d[1]
        rn = r + d[0]
        if cn >= cols or cn < 0 or rn < 0 or rn >= rows:
            continue
        if topmap[rn][cn] == "@":
            count += 1
    return True if count < 4 else False


topmap_next = deepcopy(topmap)
removed = True

original = 0
remaining = 0

for r in range(rows):
    for c in range(cols):
        if topmap[r][c] == "@":
            original += 1

while removed:
    accessibles = []
    removed = False
    for r in range(rows):
        for c in range(cols):
            if topmap_next[r][c] == "@":
                accessible = check_access(topmap, r, c)
                accessibles.append(accessible)
                if accessible:
                    topmap_next[r][c] = "."
                    removed = True
    topmap = deepcopy(topmap_next)

for r in range(rows):
    for c in range(cols):
        if topmap[r][c] == "@":
            remaining += 1

for t in topmap:
    print(*t)

print(original - remaining)
