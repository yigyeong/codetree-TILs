n = int(input())
sum_value = 0

for i in range(1, 101):
    sum_value += i
    if sum_value >= n:
        print(i)
        break