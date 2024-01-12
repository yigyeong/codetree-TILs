n1, n2 = map(int, input().split())
n1_seq = list(map(int, input().split()))
n2_seq = list(map(int, input().split()))

if n2_seq in n1_seq:
    print('Yes')
else:
    print('No')