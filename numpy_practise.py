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

ar_zero = np.zeros(4)
print(ar_zero)

ar_zero1 = np.zeros((3,4))
print(ar_zero1)


# ONES ARRAY

ar_ones = np.ones(4)
print(ar_ones)

ar_ones1 = np.ones((3,4))
print(ar_ones1)


# EMPTY ARRAY

ar_emp = np.empty(4)
print(ar_emp) # This will take up the values of previous memory


# RANGE OF ARRAY

ar_range = np.arange(4)
print(ar_range)


# DIAGONAL ARRAY

ar_dig = np.eye(3)
print(ar_dig)

ar_dig1 = np.eye(3,5)
print(ar_dig1)


# SPECIAL INTERVALS ARRAY LINSPACE

ar_lin = np.linspace(1,10,num = 5)
print(ar_lin)