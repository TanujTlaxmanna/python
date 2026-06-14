import numpy as np

# BASICS

x = np.array([1,2,3,4])
print(x)

y = [1,2,3,4]
print(y)

print(type(x))  #numpy ndarray
print(type(y))  # lisit

 
# ARRAYS

x = [1,2,3,4]
y = np.array(x)
print(y)

y = np.array([3,45,6,7,8])
print(y)

l = []
for i in range(1,5):
    int_1 = int(input("Enter your value"))
    l.append(int_1)

print(np.array(l))
print(y.ndim)

