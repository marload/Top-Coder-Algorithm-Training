base = int(input("base= "))

ans = []

for n in range(2, base):
    okFlag = True
    for k1 in range(base):
        for k2 in range(base):
            for k3 in range(base):
                if (k1*base*base + k2*base + k3) % n == 0 and (k1 + k2 + k3) % n != 0:
                    okFlag = False
                    break
            if not okFlag:
                break
        if not okFlag:
            break
    if okFlag:
        ans.append(n)

print(ans)
                