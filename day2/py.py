
with open('input.txt') as f:
    moves = [(line.split()[0], int(line.split()[1])) for line in f]

horizontal = 0
depth = 0
aim = 0
for move, size in moves:
    if move == "forward":
        horizontal += size
        depth += aim * size
    elif move == "up":
        aim -= size
    elif move == "down":
        aim += size

print(depth*horizontal)

