with open("puzzle_input_1.txt", "r") as f:
    gates = dict()
    for line in f.readlines():
        k, v = line.strip().split(":")
        gates[k] = v.split()

# print(gates)


def get_out(gate, seen, gates):
    if gate in seen:
        return 0
    if gate == "out":
        return 1
    seen.add(gate)
    paths = 0
    for g in gates[gate]:
        paths += get_out(g, set(seen), gates)
    return paths


count = get_out("you", set(), gates)
print(count)
