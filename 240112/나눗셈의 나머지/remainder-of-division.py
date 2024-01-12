a, b = map(int, input().split())

cnt = [0] * 9
while a > 0:
    cnt[a%b] += 1
    a = a // b

cnt = [elem ** 2 for elem in cnt]
print(sum(cnt))