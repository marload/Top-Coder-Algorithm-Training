def inputData(name):
    return input(name + "= ").split(' ')


first = inputData("first")
second = inputData("second")
unique = list(set(first+second))
count = {}

for hobby in unique:
    count[hobby] = 0
    for f, s in zip(first, second):
        if hobby == f or hobby == s:
            count[hobby] += 1


print(count[max(count, key=count.__getitem__)])
