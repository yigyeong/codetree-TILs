import sys

n = int(input())
arr = list(map(int, input().split()))

min_val = sys.maxsize
for i in range(n):
    if arr[i] < min_val:
        min_val = arr[i]

cnt = 0
for j in range(n):
    if arr[j] == min_val:
        cnt += 1

print(min_val, cnt)