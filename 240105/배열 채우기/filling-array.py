li = list(map(int, input().split()))
result = []
for elem in li:
    if elem == 0:
        break
    result.append(elem)

print(*result[::-1])