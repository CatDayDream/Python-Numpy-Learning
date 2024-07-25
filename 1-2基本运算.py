import numpy as np

a = np.array(((1, 2),
              (3, 4)))
b = np.array(((5, 6),
              (7, 8)))
print("矩阵a是：\n", a)
print("矩阵b是：\n", b)

c = a + b
print("加法运算的结果是：\n", c)

d = a / b
print("除法运算的结果是：\n", d)

e = np.dot(a, b)
print("点乘运算的结果是：\n", e)

f = a @ b  # 等价于np.matmul()函数
print("矩阵乘法的结果是：\n", f)

g = np.sqrt(a)
print("矩阵a的开平方是：\n", g)

h = np.sin(a)
print("矩阵a的正弦值是：\n", g)

i = np.cos(a)
print("矩阵a的余弦值是：\n", i)

j = np.log(a)
print("矩阵a的对数值是：\n", j)

k = np.power(a, 2)
print("矩阵a的平方是：\n", k)

l = a * 4
print("矩阵a的广播运算：\n", l)

m = a.max()
print("矩阵a中最大的值是：\n", m)

n = a.min()
print("矩阵a中最小的值是：\n", n)

o = a.sum()
print("矩阵a中所有数据的总和为：\n", o)

p = a.mean()
print("矩阵a中数据平均值是：\n", p)
