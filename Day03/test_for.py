# 从 1 到 10 所有偶数的平方
a_list = []
for i in range(1, 11):
    if (i % 2 == 0):
        a_list.append(i*i)

print(a_list)

b_list = [i*i for i in range(1, 11) if (i % 2 == 0)]

print(b_list)
