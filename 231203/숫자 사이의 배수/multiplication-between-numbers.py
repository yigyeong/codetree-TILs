a, b = map(int, input().split())

sum_val = 0
cnt = 0
for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        cnt += 1

avg = sum_val / (cnt)

print(sum_val, f'{avg:.1f}')