import numpy as np

a = np.array(((1, 2, 3),
              (4, 5, 6),
              (7, 8, 9)))

b = a[2]
print("获取第3行数据：", b)

c = a[:, 1]
print("获取第2列数据：", c)

d = a[0, 1]
print("获取1行2列数据：", d)

e = a[:, 1:3]
print("获取2-3列数据：\n", e)

f = a[0:2]
print("获取1-2行数据：\n", f)

g = a[1:3, 1:3]
print("获取2-3行，2-3列数据：\n", g)

h = a[::-1]
print("行翻转的结果是；\n", h)

i = a[:, ::-1]
print("列翻转的结果是：\n", i)

j = a[::-1, ::-1]
print("行列翻转的结果是：\n", j)

k = a[1, ::-1]
print("翻转第2行：\n", k)


