am, ae = map(int, input().split())
bm, be = map(int, input().split())

if am > bm:
    print('A')
elif am < bm:
    print('B')
elif ae > be:
    print('A')
else:
    print('B')