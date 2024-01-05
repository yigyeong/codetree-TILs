n = int(input())
li = list(map(int, input().split()))

result = []
for elem in li:
    if elem % 2 == 0:
        result.append(elem)

print(*result[::-1])