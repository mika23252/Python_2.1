import numpy as np

a = np.ones((3,2))
b = np.arange(3)
b = np.array([[i] for i in b])
print(a)
print(b)
c = a + b
print(c)

print('#########################################')

y = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(np.sum((y > 3) & (y < 9), axis=0))
print(np.sum((y > 3) & (y < 9), axis=1))
print(np.sum((y > 3) & (y < 9)))
