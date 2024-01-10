arr = list(map(int, input().split()))

cnt = [0] * 10
for elem in arr:
    if elem == 0:
        break
    elif elem // 10 != 0:
        el = elem // 10
        cnt[el] += 1

for i in range(1, 10):
    print(f'{i} - {cnt[i]}')