n = int(input())
cnt = 0

for i in range(n):
    x = int(input())

    if x % 2 != 0 and x % 3 == 0:
        cnt += x

print(cnt)