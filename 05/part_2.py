from copy import deepcopy

with open("puzzle_input_1.txt", "r") as f:
    ranges, ids = f.read().strip().split("\n\n")


ranges = ranges.split("\n")
ranges = [tuple(map(int, r.split("-"))) for r in ranges]

merged = True
count = 0

while True:
    copy = deepcopy(ranges)
    for i in range(len(ranges) - 1):
        i_start, i_end = ranges[i]
        for j in range(len(ranges)):
            j_start, j_end = ranges[j]
            if i != j:
                if i_start <= j_start <= i_end <= j_end:
                    ranges[i] = (i_start, j_end)
                    ranges[j] = (0, 0)
                if i_start <= j_start <= j_end <= i_end:
                    ranges[j] = (0, 0)
    ranges = sorted(ranges, reverse=True)
    ranges = set(ranges)
    if (0, 0) in ranges:
        ranges.remove((0, 0))
    ranges = sorted(list(ranges), reverse=True)
    if copy == ranges:
        break

fresh = 0

for r in ranges:
    fresh += r[1] - r[0] + 1

print(fresh)
