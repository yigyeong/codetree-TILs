import sys

n = int(input())
arr = list(map(int, input().split()))

max_1 = max(arr[0], arr[1])
max_2 = min(arr[0], arr[1])

for i in range(2, n):
    if arr[i] > max_1:
        max_1 = arr[i]
    elif arr[i] == max_1:
        if arr[i] > max_2:
            max_2 = arr[i]
    elif arr[i] >= max_2:
        max_2 = arr[i]

print(max_1, max_2)