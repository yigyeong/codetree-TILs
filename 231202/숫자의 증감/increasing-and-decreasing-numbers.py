c, n = input().split()

if c == 'A':
    for i in range(1, n+1):
        print(i, end=' ')
else:
    for i in range(n, 0, -1):
    print(i, end=' ')