with open("puzzle_input_1.txt", "r") as f:
    rotations = []
    for line in f:
        rot = int(line.strip().replace("R", "").replace("L", "-"))
        rotations.append(rot)

start = 50
count = 0

for rot in rotations:
    if rot < 0:
        mod, start2 = divmod(start + rot, 100)
        count += abs(mod)
        if start == 0 and start2 > 0:
            count -= 1
        elif start > 0 and start2 == 0:
            count += 1
        start = start2
    else:
        mod, start = divmod(start + rot, 100)
        count += mod


print(count)
