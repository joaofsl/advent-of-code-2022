def shape(round):
    if round[1] == "X": return 1
    if round[1] == "Y": return 2
    return 3

def outcome(round):
    if round in [["A", "X"], ["B", "Y"], ["C", "Z"]]: return 3;
    if round in [["A", "Y"], ["B", "Z"], ["C", "X"]]: return 6
    return 0

def score(round):
    return shape(round) + outcome(round)

f = open("../inputs/day-02.txt")
input = f.read()
# input = "A Y\nB X\nC Z"

instructions = [instruction.split(" ") for instruction in input.split("\n")]
total = sum([score(instruction) for instruction in instructions])
print(total)
