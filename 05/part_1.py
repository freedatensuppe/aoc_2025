with open("puzzle_input_1.txt", "r") as f:
    ranges, ids = f.read().strip().split("\n\n")


ranges = ranges.split("\n")
print(ranges)
ids = ids.split("\n")
print(ids)

count = 0

for id in ids:
    for r in ranges:
        start, end = r.split("-")
        if int(start) <= int(id) <= int(end):
            count += 1
            print(id)
            break

print(count)
