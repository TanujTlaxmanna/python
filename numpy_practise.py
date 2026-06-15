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

# var1 = np.array([1,2,3,4,5,6,7,8,9,8,7,6,5,4,43,32,1,5235,321,4,55,3,532,532,5])
# print("Data Type : ", var1.dtype)

# var2 = np.array([1.0, 2.2, 3.3, 4.0])
# print("Data Type : ", var2.dtype)

# var3 = np.array(["A", "B", "C", "D"])
# print("Data Type : ", var3.dtype)

# var4 = np.array(["A", "B", "C", "D", 1, 2, 3, 4])
# print("Data Type : ", var4.dtype)


# ARRAY CONVERSION

# x = np.array([1,2,3,4])
# print("Data Type : ", x.dtype)

# x = np.array([1,2,3,4], dtype = np.int8)
# print("Data Type : ", x.dtype)


# x1 = np.array([1,2,3,4], dtype = "f")
# print("Data Type : ", x1.dtype)

# x2 = np.array([1,2,3,4])
# new = np.float32(x2)

# print("Data Type : ", x2.dtype)
# print("Data Type : ", new.dtype)
# print(x2)
# print(new)


# x2 = np.array([1,2,3,4])
# new = np.float32(x2)
# new_1 = np.int_(new)

# print("Data Type : ", x2.dtype)
# print("Data Type : ", new.dtype)
# print("Data Type : ", new_1)
# print(x2)
# print(new)
# print(new_1)



# x3 = np.array([1,2,3,4])
# new1 = x3.astype(float)
# print("Data Type : ", x3)
# print("Data Type : ", new1)
# print(x3)
# print(new)



# ARRAY SHAPES

# var = np.array([[1,2,3,4], [3,4,5,6]])
# print(var, "\n")
# print(var.shape)


# var1 = np.array([1,2,3,4], ndmin = 10)
# print(var1, "\n")
# print(var1.ndim, "\n")
# print(var1.shape)


# RESHAPE

# var2 = np.array([1,2,3,4,5,6])
# x = var2.reshape(3,2)  # ONLY WORKS WHEN THERE ARE SUFFIECIENT NUMBER OF ELEMENTS AS NUMPY DOES NOT WORK WITH BLANK ELEMENTS 
# print(var2, "\n")
# print(x)
# print(var2.ndim)
# print(x.ndim)

# var3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# x2 = var3.reshape(2,3,2)  # ONLY WORKS WHEN THERE ARE SUFFIECIENT NUMBER OF ELEMENTS AS NUMPY DOES NOT WORK WITH BLANK ELEMENTS 
# print(var3, "\n")
# print(x2)
# print(var3.ndim)
# print(x2.ndim)

# var4 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# x3 = var4.reshape(2,3,2)  # ONLY WORKS WHEN THERE ARE SUFFIECIENT NUMBER OF ELEMENTS AS NUMPY DOES NOT WORK WITH BLANK ELEMENTS 
# print(var4, "\n")
# print(x3)
# print(var4.ndim)
# print(x3.ndim, "\n")

# ones = x3.reshape(-1)  # Makes it a 1-D array
# print(ones)
# print(ones.ndim)



# ARITHEMETIC OPERATIONS

# 1-D ARRAY

# var = np.array([1,2,3,4])
# var_add = var + 3
# print(var_add) # Adds all with 3

# var1 = np.array([1,2,3,4])
# var2 = np.array([5,6,7,8])

# var_add1 = var1 + var2
# print(var_add1)  # Adds both arrays

# varadds = np.add(var1, 3)
# print(varadds)

# varadds = np.add(var1, var2)
# print(varadds)



# var1 = np.array([1,2,3,4])
# var2 = np.array([5,6,7,8])

# var_add1 = var1 - var2
# print(var_add1)  # Subtracts both arrays

# varadds = np.subtract(var1, 3)
# print(varadds)

# varadds = np.subtract(var1, var2)
# print(varadds)




# var1 = np.array([1,2,3,4])
# var2 = np.array([5,6,7,8])

# var_add1 = var1 * var2
# print(var_add1)  # Multiplies both arrays

# varadds = np.multiply(var1, 3)
# print(varadds)

# varadds = np.multiply(var1, var2)
# print(varadds)




# var1 = np.array([1,2,3,4])
# var2 = np.array([5,6,7,8])

# var_add1 = var1 / var2
# print(var_add1.round(3))  # Divides both arrays

# varadds = np.divide(var1, 3)
# print(varadds)

# varadds = np.divide(var1, var2)
# print(varadds)




# var1 = np.array([1,2,3,4])
# var2 = np.array([5,6,7,8])

# var_add1 = var1 % var2
# print(var_add1)  # Modulus both arrays

# varadds = np.mod(var1, 3)
# print(varadds)

# varadds = np.mod(var1, var2)
# print(varadds)


# 2-D ARRAY

# var21 = np.array([[1,2,3,4], [5,6,7,8]])
# print(var21)
# print() 
# var22 = np.array([[1,2,3,4], [5,6,7,8]])
# print(var22)
# print()
# varadd2 = var21 + var22  # ADDS BOTH ARRAY
# print("\n", varadd2)



# var21 = np.array([[1,2,3,4], [5,6,7,8]])
# print(var21)
# print() 
# var22 = np.array([[1,2,3,4], [5,6,7,8]])
# print(var22)
# print()
# varadd2 = var21 - var22  # SUBTRACTS BOTH ARRAY
# print("\n", varadd2)


# var21 = np.array([[1,2,3,4], [5,6,7,8]])
# print(var21)
# print() 
# var22 = np.array([[1,2,3,4], [5,6,7,8]])
# print(var22)
# print()
# varadd2 = var21 * var22  # MULTIPLIES BOTH ARRAY
# print("\n", varadd2)



# var21 = np.array([[1,2,3,4], [5,6,7,8]])
# print(var21)
# print() 
# var22 = np.array([[1,2,3,4], [5,6,7,8]])
# print(var22)
# print()
# varadd2 = var21 / var22  # DIVIDES BOTH ARRAY
# print("\n", varadd2.round(2))


# varzz = np.array([1,2,3,4])
# varrec = np.reciprocal(varzz)
# print(varrec)



# ARITHEMETIC FUNCTIONS

# var = np.array([1,2,3,4,5,6,77])
# print(np.min(var))
# print(np.max(var))
# print(np.argmin(var))
# print(np.argmax(var))


# var1 = np.array([[2,1,3], [9,5,6]])
# print(np.min(var1, axis = 1))   # ROW WISE
# print(np.max(var1, axis = 1))
# print(np.argmin(var1, axis = 1))
# print(np.argmax(var1, axis = 1))
# print(np.min(var1, axis = 0))   # COLUMN WISE
# print(np.max(var1, axis = 0))
# print(np.argmin(var1, axis = 0))
# print(np.argmax(var1, axis = 0))

# print(np.sqrt(var))
# print(np.sin(var))
# print(np.cos(var))
# print(np.cumsum(var))



# INDEXING

# 1-D

# var = np.array([9,8,7,6])
# print(var[1])
# print(var[-3])

# 2-D

# var1 = np.array([[9,8,7], [4,5,6]])
# print(var1)
# print(var1.ndim)
# print()
# print(var1[0][1]) 
# print(var1[0,1])

# 3-D

# var2 = np.array([[[1,2], [3,4], [5,6]]])
# print(var2)
# print(var2.ndim)
# print(var2[0][2][1])
# print(var2[0,2,1])


# SLICING

# 1-D

# var = np.array([1,2,3,4,5,6,7,8,9,0])
# print(var)
# print()
# print(var[1:5])
# print(var[2:])
# print(var[:6])
# print(var[::2])
# print(var[:-1])
# print(var[:10])

# 2-D

# var1 = np.array([[1,2,3,4,5], [9,8,7,6,5], [11,12,13,14,15]])
# print(var1)
# print(var1[1,1:])


# 3-D

# var2 = np.array([[[1,2,3,4], [5,6,7,8], [9,10,11,12]]])
# print(var2)
# print(var2[0,2,:])



# ITERATIONS IN ARRAYS

# 1-D

# var = np.array([1,2,3,4,5,6,7,8])
# print(var)
# print()
# for i in var:
#     print(i)


# 2-D

# var1 = np.array([[1,2,3,4], [5,6,7,8]])
# print(var1)
# print()
# for j in var1:
#     print(j)

# print()

# for k in var1:
#     for l in k:
#         print(l)


# 3-D

# var3 = np.array([[[1,2,3], [4,5,6], [7,8,9]]])
# print(var3)
# print()

# for i in var3:
#     for j in i:
#         for k in j:
#             print(k)

# without using for loop

# var4 = np.array([[[1,2,3], [4,5,6], [7,8,9]]])
# print(var4)
# print()

# for i in np.nditer(var4):
#     print(i)

# for i in np.nditer(var4, flags = ['buffered'], op_dtypes = ["S"]): # nditer stands for N-dimensional iterator. flags=['buffered'] creates a temporary buffer where converted values are stored. Original Array [1, 2, 3] ↓ Convert temporarily [b'1', b'2', b'3'] ↓ Iterate
#     print(i)

# for indexing

# for i,data in np.ndenumerate(var4):
#     print(i,data)



# COPY VS VIEW

# var = np.array([1,2,3,4])

# co = var.copy()

# var[1] = 40

# print(var)
# print(co)


# x = np.array([9,8,7,6,5])

# vi = x.view()
# x[1] = 40
# print(x)
# print(vi)



# JOIN ARRAY

# 1-D

# var = np.array([1,2,3,4])
# var1 = np.array([9,8,7,6])

# ar = np.concatenate((var, var1))
# print(ar)


# 2-D

# vr = np.array([[1,2],[3,4]])
# vr1 = np.array([[9,8],[7,6]])

# ar_1 = np.concatenate((vr, vr1), axis = 1)
# print(ar_1)

# ar_0 = np.concatenate((vr, vr1), axis = 0)
# print(ar_0)



# var_1 = np.array([1,2,3,4])
# var_2 = np.array([9,8,7,6])

# ar_0 = np.stack((var_1, var_2), axis = 0)
# print(ar_0)

# ar_1 = np.stack((var_1, var_2), axis = 1)
# print(ar_1)

# ar_ = np.hstack((var_1, var_2))   # HORIZONTAL STACK
# print(ar_)

# ar_ = np.vstack((var_1, var_2))   # VERTICAL STACK
# print(ar_)

# ar_ = np.dstack((var_1, var_2))   # STACKING ALONG HEIGHT
# print(ar_)



# SPLIT ARRAY

# 1-D

# var = np.array([1,2,3,4,5,6])
# print(var)

# ar = np.array_split(var, 3)   # This creates 3 new array with data split within them in order
# print(ar)

# print(ar[0])
# print(ar[1])
# print(ar[2])

# 2-D

# var1 = np.array([[1,2],[3,4],[5,6]])
# print(var1)

# ar = np.array_split(var1, 3)   # This creates 3 new array with data split within them in order
# print(ar)

# print(ar[0][:])
# print(ar[0][:])
# print(ar[0][:])

# ar_2 = np.array_split(var1, 3, axis = 1)
# print(ar_2)




# SEARCH

# var = np.array([1,2,3,4,2,5,2,5,6,7])

# x = np.where(var == 2)
# print(x)

# x = np.where((var%2) == 0)
# print(x)


# SEARCH SORT

# var1 = np.array([1,2,3,4,5,6,7,8,9])

# x1 = np.searchsorted(var1, 5)
# print(x1)

# x1 = np.searchsorted(var1, [5,6,7], side = "right")   # Starts searching from right side
# print(x1)



# SORT

# var_1 = np.array([4,2,3,1,22,12,15,5,6,7])
# print(np.sort(var_1))


# var_2 = np.array(["a", "s", "d", "f"])
# print(np.sort(var_2))


# var_3 = np.array([[4,2,3],[1,22,12],[15,5,6]])  # 2-D ARRAY
# print(np.sort(var_3))



# FILTER

# var_4 = np.array(["a", "s", "d", "f"])
# f = [True, False, False, True]

# new_a = var_4[f]
# print(new_a)
# print(type(new_a))



# SHUFFLE

# var = np.array([1,2,3,4,5])
# np.random.shuffle(var)
# print(var)


# UNIQUE

# var1 = np.array([1,2,3,4,2,3,4,6,7])
# x = np.unique(var1)
# print(x)

# x = np.unique(var1, return_index = True)
# print(x)

# x = np.unique(var1, return_counts = True)
# print(x)


# RESIZE

# var2 = np.array([1,2,3,4,5,6])
# y = np.resize(var2, (2,3))
# print(y)

# y = np.resize(var2, (3,2))
# print(y)


# FLATTEN AND RAVEL   # THIS CONVERTS 2-D ARRAY INTO 1-D ARRAY

# var3 = np.array([1,2,3,4,5,6])
# y = np.resize(var2, (3,2))
# print(y) 

# print(y.flatten())
# print(y.flatten(order = "F"))

# print(np.ravel(y))
# print(np.ravel(y, order = "A"))




# INSERT

var = np.array([1,2,3,4])
print(var)
print(var.dtype)

v = np.insert(var, 2, 40)
print(v)

v = np.insert(var, (2,3,4), 40)   # This will only assign integer value and no floating
print(v)

x = np.append(var, 6.5)
print(x)

# 2-D

var1 = np.array([[1,2,3], [4,5,6]])
v1 = np.insert(var1, 2, 6, axis = 0)
print(v1)

v1 = np.insert(var1, 2, [22,23], axis = 1)
print(v1)

v1 = np.insert(var1, 2, 6, axis = 1)
print(v1)

v1 = np.insert(var1, 2, [22,23], axis = 1)
print(v1)

v1 = np.append(var1, [[45,23,42]], axis = 0)
print(v1)




# DELETE

var2 = np.array([1,2,3,4])
print(var2)
print(var2.dtype)

d = np.delete(var2, 2)
print(d)