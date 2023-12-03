a, b = map(int, input().split())

sum = 0
b = max(a, b)
a = min(a, b)
for i in range(a, b+1):
    if i % 5 == 0:
        sum += i

print(sum)