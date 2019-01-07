def inputData(name):
    return [int(i) for i in input(name + "= ").split(' ')]


capacities = inputData("capacities")
bottles = inputData("bottles")
fromId = inputData("fromId")
toId = inputData("toId")

for fromIdx, toIdx in zip(fromId, toId):
    residual = capacities[toIdx] - bottles[toIdx]
    if residual <= bottles[fromIdx]:
        bottles[fromIdx] -= residual
        bottles[toIdx] += residual
    else:
        bottles[toIdx] += bottles[fromIdx]
        bottles[fromIdx] = 0


print("Return:", end=' ')
for i in bottles:
    print(i, end=' ')
