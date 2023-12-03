n = int(input())

for i in range(1, 1+n):
    if i % 2 == 0:
        continue
    if i == 5:
        continue
    elif i >= 100 and i % 100 == 5:
        i = i // 100
        continue
    if i >= 10 and i % 10 == 5:
            continue
    if i % 3 == 0 and i % 9 != 0:
        continue

    print(i, end=' ')