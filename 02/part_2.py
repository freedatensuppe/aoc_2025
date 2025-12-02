with open("puzzle_input_1.txt", "r") as f:
    ranges = f.read().strip().split(",")

invalid = set()

test = set(
    [
        11,
        22,
        99,
        111,
        999,
        1010,
        1188511885,
        222222,
        446446,
        38593859,
        565656,
        824824824,
        2121212121,
    ]
)

for r in ranges:
    start, end = r.split("-")
    #    print(start, end)
    nums = [str(i) for i in range(int(start), int(end) + 1)]
    # print(nums)
    for num in nums:
        half = len(num) // 2
        if num[half:] == num[:half]:
            invalid.add(int(num))
        parts = set()

        for i in range(len(num) // 2):
            for j in range(i + 1, len(num) // 2 + 1):
                if len(num[i:j]) >= 2 and len(num[i:j]) < len(num) // 2:
                    parts.add(num[i:j])
        #        print(num, parts)
        for part in parts:
            if num.replace(part, "") == "":
                invalid.add(int(num))
                break

        for i in range(10):
            if num.replace(str(i), "") == "" and len(num) > 1:
                invalid.add(int(num))
                break


# print(sorted(test))
# print(sorted(invalid))

# print()
# print("Diff 1:", *test.difference(invalid))
# print("Diff 2:", *invalid.difference(test))
# print()

print(sum(invalid))
