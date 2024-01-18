n = int(input())
arr = list(map(int, input().split()))

m = max(arr)
cnt = 0
for elem in arr:
    if m == elem:
        cnt+= 1
    if cnt == 2:
        arr.remove(m)
        arr.remove(m)
        m = max(arr)
        cnt = 0
    
if cnt == 1:
    print(m)
else:
    print(-1)