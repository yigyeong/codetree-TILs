n = int(input())

for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range(2*(n-i-1)+1, 0, -1):
        print('*', end=' ')
    print()
for i in range(n-1):
    for j in range(n-i-2):
        print(' ', end=' ')
    for j in range(3+(2*i)):
        print('*', end=' ')
    print()