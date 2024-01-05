n = int(input())

al = 64
for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range(n-i):
        al += 1
        if al == 64+27:
            al = 65
        print(chr(al), end=' ')

    print()