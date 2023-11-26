a = list(input().split())
b = list(input().split())
a[0] = int(a[0])
b[0] = int(b[0])

if (a[1] == 'M' and a[0] >= 19) or (b[1] == 'M' and b[0] >= 19):
    print(1)
else:
    print(0)