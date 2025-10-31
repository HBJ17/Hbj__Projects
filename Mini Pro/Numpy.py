import numpy as np

x = np.array([1,2,3,5,43,4,56,7,2,4,66,54])

print(np.max(x))
print(np.min(x))
print(np.sum(x))
print(np.mean(x))
print(np.median(x))
print(np.std(x))

y = np.array([[1,2],[1,2]])
z = np.array([[1,2],[1,2]])

print(np.add(y,z))
print(np.dot(y,z))
print(y.T)
print(y.shape)