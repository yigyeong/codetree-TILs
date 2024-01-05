n = int(input())

al = 64
for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range(n-i):
        al += 1
        print(chr(al), end=' ')
    print()