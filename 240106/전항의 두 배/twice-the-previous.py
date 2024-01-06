arr=[0, 0]
arr[0], arr[1] = map(int, input().split())

for i in range(2, 10):
    arr.append(arr[i-1]+2*arr[i-2])

print(*arr)