n = int(input())

sum_val = 0

for i in range(n):
    x = int(input())
    sum_val += x

print(sum_val, f'{sum_val/n:.1f}')