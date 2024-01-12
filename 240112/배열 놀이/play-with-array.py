n, q = map(int, input().split())
num = list(map(int, input().split()))

for i in range(q):
    qst = list(map(int, input().split()))
    
    if qst[0] == 1:
        print(num[qst[1]-1])
    elif qst[0] == 2:
        if qst[1] in num:
            print(num.index(qst[1])+1)
        else:
            print(0)
    elif qst[0] == 3:
        print(*num[qst[1]-1:qst[2]])