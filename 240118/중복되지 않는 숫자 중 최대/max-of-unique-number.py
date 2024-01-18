n = int(input())
arr = list(map(int, input().split()))

m = max(arr)
cnt = 0
for elem in arr:
    if cnt > 1:
        cnt = 0
        arr.remove(m)
        arr.remove(m)
        m = max(arr)
    if m == elem:
        cnt+= 1
    
if cnt == 1:
    print(m)
else:
    print(-1)