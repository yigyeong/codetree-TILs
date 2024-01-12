n1, n2 = map(int, input().split())
n1_seq = list(map(int, input().split()))
n2_seq = list(map(int, input().split()))

cnt = 0
if n2_seq[0] in n1_seq:
    for i in range(1, len(n1_seq)-n1_seq.index(n2_seq[0])+1):
        if n2_seq[i] != n1_seq[n1_seq.index(n2_seq[0])+i]:
            break
        else:
            cnt += 1

if cnt > 0:
    print('Yes')
else:
    print('No')