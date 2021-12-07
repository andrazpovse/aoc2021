with open('input.txt') as f:
    positions = [int(i) for i in f.readline().split(",")]

price = "increasing"

def step_cost(moves):
    if price == "increasing":
        return moves * (moves + 1) / 2
    else:
        return moves

cost = []
for align_pos in range(max(positions)):
    cost.append(0)
    for pos in positions:
        cost[-1] += step_cost(abs(pos-align_pos))

print(min(cost))