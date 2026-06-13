# SERIES

import pandas as pd

# x = [3,4,5,6,7,8,9]
# a = pd.Series(x, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'], dtype = "float", name = "Pythong")
# print(a)
# print(type(a))
# print(x[5])

# dic = {"Name" : ["Python", "Java", "C#", "C++"],
#         "Por" : [12,13,14,15],
#         "Rank" : [1,4,3,2]}

# var1 = pd.Series(dic)
# print(var1)

# s = pd.Series(12, index = [1,2,3,4,5,6,7])
# print(s)
# print(type(s))

# s1 = pd.Series(12, index = [1,2,3,4,5,6,7])
# s2 = pd.Series(12, index = [1,2,3,4])

# print(s1+s2)


# DATAFRAMES - 2D STRUCTURE

# using lists
# l = [1,2,3,4,5,6]
# var = pd.DataFrame(l)
# print(var)
# print(type(var))

# list1 = [[1,2,3,4,5], [6,7,8,9,0]]
# var2 = pd.DataFrame(list1)
# print(var2)

# using dictionaaries

# d = {"a" : [1,2,3,4,5],
#      "b" : [6,7,8,9,0]}

# var1 = pd.DataFrame(d)
# print(var1)
# print(type(var1))

# specific columns

# var1 = pd.DataFrame(d, columns= ["a"], index = ["a", "b", "c", "d", "e"])
# print(var1, "\n")
# print(d["a"][3])


# Using series

# sr = {"s" : pd.Series([1,2,3,4,5]),
#       "r" : pd.Series([6,7,8,9,0])}

# var3 = pd.DataFrame(sr, index = [0,1,2,3,4])
# print(var3)


# Arithmetic Operations

# var = pd.DataFrame({"A" : [1,2,3,4,5],
#                     "B" : [6,7,8,9,0]})

# print(var)

# var["C"] = var["A"] + var["B"]
# print(var)

# var["D"] = var["C"] - var["A"]
# print(var)

# var["E"] = var["C"] * var["A"]
# print(var)

# var["F"] = var["C"] / var["A"]
# print(var.round(2))

# var1 = pd.DataFrame({"A" : [15,22,33,64,12],
#                     "B" : [60,75,8,9,0]})

# var1["Python"] = var1["A"] <=20
# var1["Python2"] = var1["B"] >=19
# print(var1)


# INSERTION AND DELETION

# var = pd.DataFrame({"A" : [1,2,3,4,5],
#                     "B" : [9,8,7,6,5],
#                     "C" : [11,12,34,5,6]})
# print(var)

# var.insert(1, "Python", var["A"])
# print(var)

# var.insert(1, "Python_1", [11,12,13,14,15])
# print(var)

# var["Python_12"] = var["A"][:3]


# DELETION

# var1 = var.pop("B")

# print(var, "\n")
# print(var1)

# del var["A"]
# print(var)


# CREATING CSV FILES USING PANDAS

# p = pd.DataFrame({"A" : [1,2,3,4,5,6],
#                   "B" : [1,2,3,4,5,6],
#                   "C" : [1,2,3,4,5,6]})
# print(p)

# p.to_csv("Test_new.csv", index= False)

# csv_1 = pd.read_csv("C:\\Users\\Office Pc\\OneDrive\\Desktop\\paithan\\Test_new.csv")
# print(csv_1)


# csv_2 = pd.read_csv("C:\\Users\\Office Pc\\OneDrive\\Desktop\\paithan\\Test_new.csv", nrows=5, usecols= [0, 1]) #or ["A", "B"]
# print(csv_2)
# print(type(csv_2))

# csv_3 = pd.read_csv("C:\\Users\\Office Pc\\OneDrive\\Desktop\\paithan\\Test_new.csv", skiprows= [0])
# print(csv_3)

# csv_4 = pd.read_csv("C:\\Users\\Office Pc\\OneDrive\\Desktop\\paithan\\Test_new.csv", index_col= "A")
# print(csv_4)


# csv_5 = pd.read_csv("C:\\Users\\Office Pc\\OneDrive\\Desktop\\paithan\\Test_new.csv", header= 4)
# print(csv_5)

# csv_6 = pd.read_csv("C:\\Users\\Office Pc\\OneDrive\\Desktop\\paithan\\Test_new.csv", names= ["Col"], dtype={"C" : "float"})
# print(csv_6)


# Pandas Functions

p = pd.DataFrame({"A" : [1,2,3,4,5,6],
                  "B" : [1,2,3,4,5,6],
                  "C" : [1,2,3,4,5,6]})

csv_1 = pd.read_csv("stocks.csv")
print(csv_1)

print(csv_1.index)
print(csv_1.columns)

print(csv_1.describe())
print(csv_1.head())
print(csv_1.tail())
print(csv_1.head(2))
print(csv_1.tail(3))
print(csv_1[:2])
print(csv_1[3:9])
print(type(csv_1))
print(csv_1.index.array)
print(csv_1.to_numpy())

import numpy as np
v = np.asarray(csv_1)
print(v)

print(csv_1.sort_index(axis=0, ascending= False))

csv_1.loc[0, "Symbol"] = "Python"
print(csv_1)

print(csv_1.loc[[2,3], ["Symbol", "Company Name"]])

print(csv_1.iloc[0, 2])

print(csv_1.drop("Company Name", axis = 1))
print(csv_1)