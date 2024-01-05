li = list(map(int, input().split()))

re_li = []
sum_val = 0
for i in range(10):
    if li[i] < 250:
        re_li.append(li[i])
        sum_val += re_li[i]
    else:
        break

n = len(re_li)
print(f'{sum_val} {sum_val/n:.1f}')