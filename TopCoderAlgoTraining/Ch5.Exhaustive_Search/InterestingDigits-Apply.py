base = int(input("base="))

ans = []

for n in range(2, base):
    if ((base - 1) % n) == 0:
        ans.append(n)

print(ans)

'''
Explain
1. base-1이 n의 배수라면 n은 그 조건에 충족
'''
