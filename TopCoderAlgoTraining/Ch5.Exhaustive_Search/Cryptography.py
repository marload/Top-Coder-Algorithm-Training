def inputData(name):
    return [int(i) for i in input(name + "= ").split(' ')]


capacities = inputData("capacities")

capacities[capacities.index(min(capacities))] += 1

answer = 1
for i in capacities:
    answer *= i

print(answer)
