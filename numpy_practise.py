import numpy as np

# # BASICS

# x = np.array([1,2,3,4])
# print(x)

# y = [1,2,3,4]
# print(y)

# print(type(x))  #numpy ndarray
# print(type(y))  # lisit

 
# ARRAYS

# x = [1,2,3,4]
# y = np.array(x)
# print(y)

# y = np.array([3,45,6,7,8])
# print(y)

# l = []
# for i in range(1,5):
#     int_1 = int(input("Enter your value"))
#     l.append(int_1)

# print(np.array(l))
# print(y.ndim)

# TYPES OF ARRAYS 
# 1 DIMENSIONAL
# 2 DIMENSIONAL
# 3 DIMENSIONAL
# MULTI / HIGHER DIMENSIONAL

# 1-D

# x = [1,2,3,4]
# y = np.array(x)
# print(y.ndim)

# 2-D

# ar2 = np.array([[1,2,3,4],[5,6,7,8]]) # number of data should be same
# # ar3 = np.array([[1,2,3,4],[5,6,7]]) # will throw error
# print(ar2)
# print(ar2.ndim)


# 3-D

# ar3 = np.array([[[1,2,3,4], [5,6,7,8], [0,9,8,7]]])
# print(ar3)
# print(ar3.ndim)

# N-D

# arn = np.array([1,2,3,4], ndmin = 10)  # we use ndmin for specifying dimensions
# print(arn)
# print(arn.ndim)


# Special Types of NumPy Array

# ZERO ARRAY

# ar_zero = np.zeros(4)
# print(ar_zero)

# ar_zero1 = np.zeros((3,4))
# print(ar_zero1)


# ONES ARRAY

# ar_ones = np.ones(4)
# print(ar_ones)

# ar_ones1 = np.ones((3,4))
# print(ar_ones1)


# EMPTY ARRAY

# ar_emp = np.empty(4)
# print(ar_emp) # This will take up the values of previous memory


# RANGE OF ARRAY

# ar_range = np.arange(4)
# print(ar_range)


# DIAGONAL ARRAY

# ar_dig = np.eye(3)
# print(ar_dig)

# ar_dig1 = np.eye(3,5)
# print(ar_dig1)


# SPECIAL INTERVALS ARRAY LINSPACE

# ar_lin = np.linspace(1,10,num = 5)
# print(ar_lin)



# RANDOMS

# RAND()

# var = np.random.rand(4)
# print(var)

# var1 = np.random.rand(2,5)   # 2-D array
# print(var1)


# RANDN()

# var2 = np.random.randn(5)
# print(var2)

# var3 = np.random.randn(3,5) # 2-D array
# print(var3)


# RANF()

# var4 = np.random.ranf(4)
# print(var4)

# var5 = np.random.ranf((4,5)) # 2-D ARRAY
# print(var5)

# RANDINT()

# var6 = np.random.randint(5,20,5)
# print(var6)

# var7 = np.random.randint(5,20,(4,5)) #2-D ARRAY
# print(var7)


# DATA TYPES

var1 = np.array([1,2,3,4,5,6,7,8,9,8,7,6,5,4,43,32,1,5235,321,4,55,3,532,532,5])
print("Data Type : ", var1.dtype)

var2 = np.array([1.0, 2.2, 3.3, 4.0])
print("Data Type : ", var2.dtype)

var3 = np.array(["A", "B", "C", "D"])
print("Data Type : ", var3.dtype)

var4 = np.array(["A", "B", "C", "D", 1, 2, 3, 4])
print("Data Type : ", var4.dtype)


# ARRAY CONVERSION

x = np.array([1,2,3,4])
print("Data Type : ", x.dtype)

x = np.array([1,2,3,4], dtype = np.int8)
print("Data Type : ", x.dtype)


x1 = np.array([1,2,3,4], dtype = "f")
print("Data Type : ", x1.dtype)

x2 = np.array([1,2,3,4])
new = np.float32(x2)

print("Data Type : ", x2.dtype)
print("Data Type : ", new.dtype)
print(x2)
print(new)


x2 = np.array([1,2,3,4])
new = np.float32(x2)
new_1 = np.int_(new)

print("Data Type : ", x2.dtype)
print("Data Type : ", new.dtype)
print("Data Type : ", new_1)
print(x2)
print(new)
print(new_1)



x3 = np.array([1,2,3,4])
new1 = x3.astype(float)
print("Data Type : ", x3)
print("Data Type : ", new1)
print(x3)
print(new)