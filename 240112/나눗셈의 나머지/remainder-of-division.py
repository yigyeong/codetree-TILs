a, b = map(int, input().split())

cnt = [0] * 9
while:
    cnt[a%b] += 1
    a = a // b
    if a < 1:
        break

cnt = [elem ** 2 for elem in cnt]
print(sum(cnt))