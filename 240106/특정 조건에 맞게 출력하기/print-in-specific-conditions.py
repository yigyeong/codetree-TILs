arr = list(map(int, input().split()))
arr2 = [elem for elem in arr if elem != 0]

for i in range(len(arr2)):
    if arr2[i] % 2 == 0:
        arr2[i] //= 2
    else:
        arr2[i] += 3

print(*arr2)