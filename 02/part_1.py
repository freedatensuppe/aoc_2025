with open("puzzle_input_1.txt", "r") as f:
    ranges = f.read().strip().split(",")

invalid = []

for r in ranges:
    start, end = r.split("-")
    nums = [str(i) for i in range(int(start), int(end) + 1)]
    for num in nums:
        half = len(num) // 2
        if num[half:] == num[:half]:
            invalid.append(int(num))

print(invalid)
print(sum(invalid))
