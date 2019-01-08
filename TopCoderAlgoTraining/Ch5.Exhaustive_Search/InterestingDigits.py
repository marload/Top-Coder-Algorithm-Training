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

'''
Explain
1. 3자리 이하라는 조건이 있으니 3자리 이하의 base진법 수를 모두 구함
2. 구해진 수가 n의 배수이지만((k1*base*base + k2*base + k3) %n ==0) 각 자리의 합이 n의 배수가 아니라면 okFlag를 False로 셋팅함
'''
