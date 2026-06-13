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

# p = pd.DataFrame({"A" : [1,2,3,4,5,6],
#                   "B" : [1,2,3,4,5,6],
#                   "C" : [1,2,3,4,5,6]})

# csv_1 = pd.read_csv("stocks.csv")
# print(csv_1)

# print(csv_1.index)
# print(csv_1.columns)

# print(csv_1.describe())
# print(csv_1.head())
# print(csv_1.tail())
# print(csv_1.head(2))
# print(csv_1.tail(3))
# print(csv_1[:2])
# print(csv_1[3:9])
# print(type(csv_1))
# print(csv_1.index.array)
# print(csv_1.to_numpy())

# import numpy as np
# v = np.asarray(csv_1)
# print(v)

# print(csv_1.sort_index(axis=0, ascending= False))

# csv_1.loc[0, "Symbol"] = "Python"
# print(csv_1)

# print(csv_1.loc[[2,3], ["Symbol", "Company Name"]])

# print(csv_1.iloc[0, 2])

# print(csv_1.drop("Company Name", axis = 1))
# print(csv_1)


# DROP NA AND FILL NA
# var = pd.read_csv("stocks.csv")
# var.dropna() #This drops all nan columns
# var.dropna(axis= 0)
# var.dropna(how= "any")  #This drops all the rows which have atleast one nan
# var.dropna(how= "all")  #This only drops the row which has all nan value
# var.dropna(subset= ["Change"]) #Removes a null value along column
# var.dropna(inplace= True) #This directly makes changes to the original dataset instead of creating a copy
# var.dropna(thresh= 1) #This drops only single null value

# var.fillna("Python") #Fills/Replaces nan value with python
# var.fillna({"Symbol" : "python",
#             "Company Name" : "Python2"}) #This replaces nan in specified columns so any nan in symbol column gets replaced by python and so on
# var.fillna(method = "ffill") #Fills with leading data
# var.fillna(method = "bfill") #FIlls with trailing data
# var.fillna(method = "bfill", axis = 0) #FIlls with trailing data alongside columns. Takes data from above value , default
# var.fillna(method = "bfill", axis = 1) #FIlls with trailing data alongside rows. Takes data from left value
# var.fillna(12, inplace= True) #This directly makes changes to the original dataset instead of creating a copy. Fills with 12
# var.fillna("python", limit = 2) #Fills the first 2 Nan data from top to bottom


# REPLACE

# var = pd.read_csv("stocks.csv")

# var.replace(to_replace = 1, value=22) #Replaces all singular 1 in dataset with 22
# var.replace(to_replace= "ABC Industries Limited", value= "python")
# var.replace([1,2,3,4,5,6,7,8,9,10,11,12,13,14], 22) #Replaces 1-14 with 22  
# var.replace("[A-za-z]", "python", regix = True) #Here we dont use comma because regix dont use comma to seperate, it will also replace all the instances of the letter with python so abc = pythonpythonpython
# var.replace({"Symbol" : "[A-Z]"}, 22, regix = True) #Same as above but replaces specific column
# var.replace(1, method = "ffill") #Replaces all singlular ones in dataset with above number
# var.replace(1, method = "bfill") #Replaces all singlular ones in dataset with below number
# var.replace(1, method = "ffill", limit =2) #Replaces first 2 instances of singular 1
# var.replace(1, method = "ffill", limit = 3, inplace= True) #will replace in the original dataset

# INTERPOLATE - automatically replaces nan values with sequence of previous data

# var = pd.read_csv("stocks.csv")

# var.interpolate() #only works with numerical data
# var.interpolate(method = "linear") #fills data linearly
# var.interpolate(method = "linear", axis = 1) #This happens only when all work is done numerically, cannot work with strings
# var.interpolate(limit = 2) #Fills only 2 nan values
# var.interpolate(limit_direction= "forward" ,limit = 2) #from top to bottom
# var.interpolate(limit_direction= "backward" ,limit = 2) #from bottom to top
# var.interpolate(limit_direction= "both" ,limit = 2) #from top to bottom and bottom to top
# var.interpolate(limit_area = "inside") #fills only all nan data that are in between of 2 valid values - 3 4 nan nan 5
# var.interpolate(limit_area = "outside") #fills only the blank data at beginning and ending of dataset nan nan 3 4 nan nan
# var.interpolate(limit_direction = "both", limit = 2, inplace = "True") #will make changes in orignal dataset



# MERGING DATAFRAMES

# var1 = pd.DataFrame({"A" : [1,2,3,4],
#                      "B" : [11,12,13,14]})
# var2 = pd.DataFrame({"A" : [1,2,3,4],
#                      "C" : [91,25,53,41]})

# print(var1)
# print(var2, "\n")
# print(pd.merge(var1, var2, on = "A"))
# print(pd.merge(var2, var1, on = "A"))

# var3 = pd.DataFrame({"A" : [1,2,3,4],
#                      "B" : [11,12,13,14]})
# var4 = pd.DataFrame({"A" : [1,2,3,44],
#                      "C" : [91,25,53,41]})

# print(pd.merge(var3, var4, on = "A"))
# print(pd.merge(var4, var3, on = "A"))

# acts like joints from sql - left, right, outer, inner
# pd.merge(var3, var4, how = "outer")  #left prints all value in var 3 and puts nan in var 4 where value is not there, right does the same with var 4 and var 3, outer will make union and print all teh valeus and nan in missing places , inner will find intersection points and print only common points 

# pd.merge(var3, var4, how= "outer", indicator= True) #shows what data are missing and what are present - both, left_only, right_only

# var1 = pd.DataFrame({"A" : [1,2,3,4],
#                      "B" : [11,12,13,14]})
# var2 = pd.DataFrame({"A" : [1,2,3,4],
#                      "B" : [91,25,53,41]})
# pd.merge(var1, var2, left_index= True, right_index= True) #Normally since both A and B are common we wont get a table, but with left and right index we will get the data in form of ax, bx, ay, by
# pd.merge(var1, var2, left_index= True, right_index= True, suffixes = ("names", "id")) #gives suffixes and replaces ax, bx with names and ay, by with id

# COCNCAT

# sr1 = pd.Series([1,2,3,4])
# sr2 = pd.Series([11,21,31,41])

# sr1
# sr2

# pd.concat([sr1, sr2]) #concats series 1 and series 2
# pd.concat([var1, var2]) #concates dict1 and dict2, this does not care about common parts
# pd.concat([var1, var2], axis = 1) #column wise
# pd.concat([var1, var2], axis = 0) #rowwise, default


# var1 = pd.DataFrame({"A" : [1,2,3,4],
#                      "B" : [11,12,13,14]})
# var2 = pd.DataFrame({"A" : [1,2],
#                      "B" : [91,25,53,41]})

# pd.concat([var1, var2], axis = 1) #this will concat both dicts and show nan in missing places
# pd.concat([var1, var2], axis = 1, join = "inner") #will not show missing data
# pd.concat([var1, var2], axis = 0, join = "inner" , keys = ["A", "B"]) #gives title and shows blocks of merges

# var1 = pd.DataFrame({"A" : [1,2,3,4]})
# var2 = pd.DataFrame({"B" : [1,2],
#                      "C" : [91,25,53,41]})

# pd.concat([var1, var2]) #This will also merge and show nan in missing places


# GROUP BY

# var = pd.DataFrame({
#     "name" : ["a", "b", "c", "d", "a", "a", "b", "a", "c", "c", "a"],
#     "subject1" : [12, 13, 14, 12, 14, 15, 23, 25, 16, 23, 13],
#     "subject2" : [23,12,12,14,15,23,19,10,23,25,12]
# })

# var

# var_New = var.groupby("name") #grouping/ arranging by name column

# for x,y in var_New : 
#     print(x)
#     print(y, "\n")

# print(var_New.get_group("a")) #printing singular groups

# var_New.min() #min value of s1 and s2
# var_New.max()  #max value of s1 and s2
# var_New.mean() #mean of s1 and s2

# li = list(var_New) #converting to list


# JOIN AND APPEND

# var1 = pd.DataFrame({
#     "A" : [1,2,3,4],
#     "B" : [11,12,13,14]
# }, index= ["a", "b", "c", "d"])

# var2 = pd.DataFrame({
#     "C" : [10,20,30,40],
#     "D" : [11,22,33,44]
# }, index= ["a", "b", "c", "d"])   #both dataframes must have same indexes or else we will get nan

# print(var1.join(var2))  #joins var 2 with var 1, incase there are missing, unamtched values then it shows nan 
# var2.join(var1) #this will revers C D then A B, incase if var2 has less data like 2 as comapred to var 1 which has 4 then it will print only 2 rows

# var2.join(var1, how = "outer") #prints all even if theres any missing, fills nan with missing   
# var2.join(var1, how = "inner") #prints only intersections 

# var1 = pd.DataFrame({
#     "A" : [1,2,3,4],
#     "B" : [11,12,13,14]
# }, index= ["a", "b", "c", "d"])

# var2 = pd.DataFrame({
#     "C" : [10,20,30,40],
#     "B" : [11,22,33,44]
# }, index= ["a", "b", "c", "d"]) #Simialar column name

# var2.join(var1, how = "outer", lsuffix = "_l2") #this will for the runtime make the left side B as B_l2 and add a suffix
# var2.join(var1, how = "outer", Rsuffix = "_l2") #this will for the runtime make the right side B as B_l2 and add a suffix
# var2.join(var1, how = "outer", lsuffix = "l2", Rsuffix = "_l2") #this will work too since for the runtime we are distinguising right and left sides of B


# APPEND

# var1 = pd.DataFrame({
#     "A" : [1,2,3,4],
#     "B" : [11,12,13,14]
# }, index= ["a", "b", "c", "d"])

# var2 = pd.DataFrame({
#     "C" : [10,20,30,40],
#     "B" : [11,22,33,44]
# }, index= ["a", "b", "c", "d"]) #Simialar column name

# var1.append(var2) #similar to concat does not affect itself even if there are name clashing however in pandas 2.0 append has been removed so this will throw an error


# MELT() FUNCTION - denotes data in single column

# var = pd.DataFrame({
#     "days" : [1,2,3,4,5,6],
#     "eng" : [10,12,14,15,16,12],
#     "math" : [17,18,19,13,14,16]
# })

# pd.melt(var) #makes table verticle
# pd.melt(var, id_vars = ["days"]) #this will make indexs as days number
# pd.melt(var, id_vars = ["days"], var_name = "python", value_name = "tanuj")


# PIVOT() FUNCTION

# var = pd.DataFrame({
#     "days" : [1,2,3,4,5,6],
#     "st_name" : ["a", "b", "c", "a", "b", "c"],
#     "eng" : [10,12,14,15,16,12],
#     "math" : [17,18,19,13,14,16]
# })

# var.pivot(index = "days", columns = "st_name")  #makes a pivot table and fills nan for missing data spaces
# var.pivot(index = "days", columns = "st_name", values = "eng") #shows only english subject data
# var.pivot(index = "days", columns = "st_name")

# var = pd.DataFrame({
#     "days" : [1,1,1,1,2,2],
#     "st_name" : ["a", "b", "c", "a", "b", "c"],
#     "eng" : [10,12,14,15,16,12],
#     "math" : [17,18,19,13,14,16]
# })

# var.pivot_table(index = "st_name", columns = "days", aggfunc = "mean") #aggfunc is aggregate function
# var.pivot_table(index = "st_name", columns = "days", aggfunc = "mean", margins = "True") #margins adds a summary column like mean