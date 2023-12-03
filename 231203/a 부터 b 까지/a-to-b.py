a, b = map(int, input().split())

print(a, end = ' ')
for i in range(a, b+1):
    if i % 2 != 0:
        print(i*2, end=' ')
        i *= 2
    else:
        print(i+3, end=' ')
        i += 3