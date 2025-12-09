with open("puzzle_input_1.txt", "r") as f:
    coords = set(tuple(map(int, c.split(","))) for c in f.readlines())

print(coords)

areas = []

for i in coords:
    for j in coords:
        area = (abs(i[0] - j[0]) + 1) * (abs(i[1] - j[1]) + 1)
        areas.append(area)

print(max(areas))
