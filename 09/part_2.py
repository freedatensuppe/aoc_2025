from shapely import Polygon

with open("puzzle_input_1.txt", "r") as f:
    coords = [tuple(map(int, c.split(","))) for c in f.readlines()]


poly = Polygon(coords)
print(len(coords))

max_area = -1

for count, i in enumerate(coords):
    print(count)
    for j in coords:
        x1 = min(i[0], j[0])
        x2 = max(i[0], j[0])
        y1 = min(i[1], j[1])
        y2 = max(i[1], j[1])
        current = Polygon(((x1, y1), (x2, y1), (x2, y2), (x1, y2)))
        if poly.contains(current):
            area = (abs(i[0] - j[0]) + 1) * (abs(i[1] - j[1]) + 1)
            if area > max_area:
                max_area = area

print(max_area)
