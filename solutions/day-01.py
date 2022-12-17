f = open("../inputs/day-01.txt")
input = f.read()

max = 0
current_total = 0

for line in input.split("\n"):
    if not line:
        max = max if max > current_total else current_total
        current_total = 0
        continue

    current_total += int(line)

print(max)
