li = list(map(int, input().split()))
result = []

for elem in li:
    if elem == 0:
        break
    result.append(elem)

n = len(result)
s = sum(result)

print(f'{s} {s/n:.1f}')