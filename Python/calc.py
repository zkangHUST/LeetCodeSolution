base = 143.616
exp = 1.004
sum = 0
for i in range(22):
    sum += base * pow(exp, i)
print(sum)