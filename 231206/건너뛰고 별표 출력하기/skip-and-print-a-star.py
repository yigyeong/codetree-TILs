n = int(input())
cnt = 1

for i in range(2*n+1):
    for j in range(cnt):
        print('*', end='')
    print('\n')

    if cnt < n-1:
        cnt += 1
    else:
        cnt -= 1