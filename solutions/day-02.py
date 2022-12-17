def shape(round):
    return ord(round[1]) - 87

def outcome(round):
    diff = ord(round[1]) - ord(round[0])
    if diff == 23: return 3;
    if not diff % 3: return 6
    return 0

def score(round):
    return shape(round) + outcome(round)

f = open("../inputs/day-02.txt")
input = f.read()
# input = "A Y\nB X\nC Z"

instructions = [instruction.split(" ") for instruction in input.split("\n")]
total = sum([score(instruction) for instruction in instructions])

print("Part 1: %s" % total)
