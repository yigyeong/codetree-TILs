a, b = map(int, input().split())

print(a, end = ' ')
while a < b:
    if a % 2 != 0:
        print(a*2, end=' ')
        a *= 2
    else:
        print(a+3, end=' ')
        a += 3