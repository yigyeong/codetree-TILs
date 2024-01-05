arr = list(map(int, input().split()))

even = sum(arr[1::2])
odd = sum(arr[::2])

print(max(even, odd) - min(even, odd))