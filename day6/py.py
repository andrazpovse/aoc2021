days = 256
with open('input.txt') as f:
    lfish = [int(i) for i in f.readline().split(",")]

population = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0
}

for fish in lfish:
    population[fish] += 1

for i in range(days):
    population2 = population.copy()
    for idx in range(len(population) - 1):
        if idx == 6:
            continue
        if idx == 0:
            population2[8] = population[0]
            population2[6] = population[0] + population[7]
            
        population2[idx] = population[idx+1]
        
    population = population2.copy()


print(sum(population.values()))

