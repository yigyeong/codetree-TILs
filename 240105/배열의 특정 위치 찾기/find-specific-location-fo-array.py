li = list(map(int, input().split()))

li_2 = li[1::2]
li_3 = li[2::3]

sum_val = sum(li_2)
sum_val_3 = sum(li_3)
n = len(li_3)

print(f'{sum_val} {sum_val_3/n:.1f}')