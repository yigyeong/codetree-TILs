arr = list(map(int, input().split()))
cnt = [0] * 11

for elem in arr:
    if elem == 0:
        break
    elif elem // 10 != 0:
        cnt[elem // 10] += 1

for i in range(10, 0, -1):
    print(f'{i}0 - {cnt[i]}')