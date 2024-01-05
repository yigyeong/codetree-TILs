li = list(map(int, input().split()))
result = []
for elem in li:
    if elem == 0:
        print(*result[::-1])
    result.append(elem)