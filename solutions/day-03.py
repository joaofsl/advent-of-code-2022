f = open("../inputs/day-03.txt")
input = f.read()

def value(val):
    val = ord(val) - 38
    if val > 52: val -= 58
    return val
def part1(input):
    sum = 0
    for sack in input.split("\n"):
        l = (int)(len(sack)/2)
        c1 = sack[:l]
        c2 = sack[l:]
        v = value(list(set(c1).intersection(c2))[0])
        sum += v
    print(sum)

def part2(input):
    sacks = input.split("\n")
    sum = 0
    for i in range(0, len(sacks), 3):
        sum += value(list(set("".join(list(set(sacks[i]).intersection(sacks[i+1])))).intersection(sacks[i+2]))[0])
    print(sum)

part1(input)
part2(input)