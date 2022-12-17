def shape(round):
    return ord(round[1]) - 87

def new_shape(round):
    if round[1] == "X":
        if round[0] == "A": return "Z" 
        if round[0] == "B": return "X" 
        return "Y" 
    if round[1] == "Y":
        return chr(ord(round[0]) + 23)
    else:
        if round[0] == "A": return "Y" 
        if round[0] == "B": return "Z" 
        return "X" 

def outcome(round):
    diff = ord(round[1]) - ord(round[0])
    if diff == 23: return 3;
    if not diff % 3: return 6
    return 0

def score(round):
    return shape(round) + outcome(round)

def new_score(round):
    round[1] = new_shape(round)
    return score(round)

f = open("../inputs/day-02.txt")
input = f.read()

instructions = [instruction.split(" ") for instruction in input.split("\n")]
total = sum([score(instruction) for instruction in instructions])
new_total = sum([new_score(instruction) for instruction in instructions])

print("Part 1: %s" % total)
print("Part 2: %s" % new_total)
