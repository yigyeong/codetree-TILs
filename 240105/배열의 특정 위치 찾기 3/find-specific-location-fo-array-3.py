li = list(map(int, input().split()))
n = len(li)

for i in range(n):
    if li[i] == 0:
        sum_val = li[i-1] + li[i-2] + li[i-3]
        break

print(sum_val)