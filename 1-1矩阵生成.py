import numpy as np

a = np.zeros((3, 2))
b = np.ones((2, 3))
print("生成3x2的全0矩阵：\n", a.shape)
print("生成2x3的全1矩阵：\n", b.shape)

c = np.linspace(0, 3, 3)
print("生成的0-3等间隔数组：\n", c)

d = np.random.rand(3, 3)
print("随机生成的3x3随机数组：\n", d)
print("矩阵d的数据类型是：\n", d.dtype)

e = np.zeros((3, 2), dtype=np.int64)
print("矩阵e的数据类型是：\n", e.dtype)

f = e.astype(np.float32)
print("矩阵f的数据类型是：\n", f.dtype)
