import sys

n1, n2 = map(int, input().split())
n1_seq = list(map(int, sys.stdin.readline().split()))
n2_seq = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(n1):
    success = True

    for j in range(n2):
        if i + j >= n1:
            success = False
            break

        if n1_seq[i+j] != n2_seq[j]:
            success = False
            break
        
if success:
    print("Yes")
    sys. exit()
    
else:
    print('No')