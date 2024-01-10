hos = [0, 0, 0, 0]

for i in range(3):
    sym, tem = input().split()
    tem = int(tem)
    if tem >= 37 and sym == 'Y':
        hos[0] += 1
    elif tem >= 37 and sym == 'N':
        hos[1] += 1
    elif tem < 37 and sym == 'Y':
        hos[2] += 1
    else:
        hos[3] += 1

print(*hos, end=' ')
if hos[0]>=2:
    print('E')