n = int(input())

c = 0
l = 0
t = 0

for i in range(1, n+1):
    if i % 2 == 0:
        c += 1
        if i % 12 == 0:
            c -= 1
            t += 1
        elif i % 6 == 0:
            c -= 1
            l += 1
    elif i % 3 == 0:
        l += 1
        if i % 12 == 0:
            l -= 1
            t += 1
        
print(c, l, t)