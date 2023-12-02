a, b, c = map(int, input().split())
m = 0

if a > b and a > c:
    if b > c:
        m = b
    else:
        m = c
elif b > c and b > a:
    if a > c:
        m = a
    else:
        m = c
elif c > a and c > b:
    if a > b:
        m = a
    else:
        m = b

    
print(m)