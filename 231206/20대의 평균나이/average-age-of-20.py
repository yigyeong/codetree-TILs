sum_value = 0
p = 0
while True:
    n = int(input())
    if n < 20 or n >= 30:
        break
    sum_value += n
    p += 1
    
print(f'{sum_value/p:.2f}')