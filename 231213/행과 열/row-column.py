a, b = map(int, input().split())

for i in range(1, 1+a):
    for j in range(1, b+1):
        print(i*j, end=' ')
    print()