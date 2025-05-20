import numpy as np

a = np.array([[11, 21, 31], [3, 4, 5]])
b = np.array([[12, 22, 32], [6, 7, 8]])
c = np.array([[13, 23, 33], [9, 10, 11]])

d = np.concatenate((a, b, c), axis=1)
print(d)

 

arr = np.stack((a,b,c), axis=1)

print(arr)

stack_row = np.vstack((a, b, c))
print(stack_row)

stack_row = np.dstack((a, b, c))
print(stack_row)