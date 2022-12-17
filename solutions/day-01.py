f = open("../inputs/day-01.txt")
input = f.read()

totals = [sum([int(value) for value in food.split("\n")]) for food in input.split("\n\n")]
totals.sort(reverse=True)
print("Part 1: %s" % totals[0])
print("Part 2: %s" % sum(totals[:3]))
