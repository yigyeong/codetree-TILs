n = int(input())
arr = list(map(int, input().split()))

m = -1
for elem in arr:
    if m < elem:
        cnt = 0
        for elem2 in arr:
            if elem == elem2:
                cnt += 1
        if cnt == 1:
            m = elem
    
print(m)