a = 0

for i in range(3):
    sym, tem = input().split()
    tem = int(tem)
    if sym == 'Y':
        if tem >= 37:
            a += 1

if a >= 2:
    print('E')
else:
    print('N')