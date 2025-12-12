with open("puzzle_input_1.txt", "r") as f:
    raws = f.read().strip().split("\n\n")


areas = []
blocks = []
counts = []

for raw in raws:
    if "#" in raw:
        blocks.append(raw.count("#"))
    if "x" in raw:
        a = raw.split("\n")
        for b in a:
            c, d = b.split(":")
            areas.append(eval(c.replace("x", "*")))
            counts.append(list(map(int, (d.split()))))


print(areas)
print(blocks)
print(counts)

fits = 0

for area, count in zip(areas, counts):
    a = 0
    for b, c in zip(blocks, count):
        a += b * c

    if a < area:
        fits += 1

print(fits)
