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

var1 = pd.DataFrame({"A" : [15,22,33,64,12],
                    "B" : [60,75,8,9,0]})

var1["Python"] = var1["A"] <=20
var1["Python2"] = var1["B"] >=19
print(var1)