a, b, c = map(int, input().split())
if a > b:
    if a < c:
        m = a
    elif b > c:
        m = b
    else:
        m = c

print(m)