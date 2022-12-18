f = open("../inputs/day-03.txt")
input = f.read()

sum = 0
for sack in input.split("\n"):
    l = (int)(len(sack)/2)
    c1 = sack[:l]
    c2 = sack[l:]
    value = ord(list(set(c1).intersection(c2))[0]) - 38
    if value > 52: value -= 58
    sum += value
print(sum)
