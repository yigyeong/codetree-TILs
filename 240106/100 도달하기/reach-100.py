n = int(input())

arr = [0, 0]
arr[0] = 1
arr[1] = n

i = 2
while 1:
    arr.append(arr[i-1] + arr[i-2])
    if arr[i] > 100:
        break
    i += 1

print(*arr)