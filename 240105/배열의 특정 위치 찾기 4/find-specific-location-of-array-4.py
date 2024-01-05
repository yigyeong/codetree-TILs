li = list(map(int, input().split()))

re = []
for i in li:
    if i == 0:
        break
    elif i % 2 == 0:
        re.append(i)

n = len(re)
s = sum(re)

print(n, s)