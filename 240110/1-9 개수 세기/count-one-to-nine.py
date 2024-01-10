n = int(input())
arr = list(map(int, input().split()))

cnt = [0] * 10
for elem in arr:
    cnt[elem] += 1

for i in range(1, 10):
    print(cnt[i])