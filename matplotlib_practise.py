import matplotlib.pyplot as plt

# BASICS

x = [1,2,3,4,5]
y = [2,4,6,8,10]
c = ["r", "y", "b", "pink", "g"]

plt.bar(x, y, color=c)
plt.show()

# TYPES OF PLOTS

# BAR PLOT

# SYNTAX:
# x = []
# y = []
# plt.bar(x, y)
# plt.show()

x = ["python", "c", "c++", "java"]
y = [85, 70, 60, 82]    
z = [25, 28, 23, 33]
plt.xlabel("Languages", fontsize= 15)
plt.ylabel("Popularity", fontsize = 15)
plt.title("Popularity of Programming Languages", fontsize = 15)
c = ["y", "b", "m", "g"]
plt.bar(x, y, width = 0.5, color = c)
plt.show()
plt.bar(x, y, width = 0.5, color = c, align = "edge") # align = "edge" will align the bars to the edge of the x-axis, this is bydefault in center
plt.show()
plt.bar(x, y, width = 0.5, color = c, edgecolor = "black", linewidth = 2) # edgecolor will add a border to the bars, linewidth will set the width of the border
plt.show()
plt.bar(x, y, width = 0.5, color = c, edgecolor = "black", linewidth = 2, linestyle = ":") # linestyle will set the style of the border, it can be solid, dashed, dotted, dashdot
plt.show()
plt.bar(x, y, width = 0.5, color = c, edgecolor = "black", linewidth = 2, hatch = "/") # hatch will add a pattern to the bars
plt.show()
plt.bar(x, y, width = 0.5, color = c, edgecolor = "black", linewidth = 2, linestyle = ":", alpha = 0.5) # alpha will set the transparency of the bars, it can be a value between 0 and 1
plt.show()
plt.bar(x, y, width = 0.5, color = c, edgecolor = "black", linewidth = 2, linestyle = ":", alpha = 0.5, label = "Popularity") # label will add a label to the bars, it is used in legend
plt.legend() # legend will show the label of the bars
plt.show() 

# STACKED BAR GRAPHS

# STACKED ON TOP OF EACH OTHER
plt.bar(x, y, width = 0.5, color = c, label = "Popularity")
plt.bar(x, z, width = 0.5, color = "r", label = "Interest")
plt.legend()
plt.show()

# STACKED SIDE BY SIDE
import numpy as np

width = 0.2
p = np.arange(len(x))
p1 = [j + width for j in p]


plt.bar(p, y, width, color = c, label = "Popularity")
plt.bar(p1, z, width, color = "r", label = "Interest")

plt.xticks(p + width/2 , x, rotation = 10) # rotation is optional
plt.legend()
plt.show()


# HORIZONTAL BAR GRAPHS
x = ["python", "c", "c++", "java"]
y = [85, 70, 60, 82]    
z = [25, 28, 23, 33]
plt.xlabel("Languages", fontsize= 15)
plt.ylabel("Popularity", fontsize = 15)
plt.title("Popularity of Programming Languages", fontsize = 15)

plt.barh(x, y, color = "g", label = "Popularity")
plt.barh(x, z, color = "r", label = "Interest")
plt.legend()
plt.show()


# HORIZONTAL STACKED BAR SIDE BY SIDE GRAPHS

import numpy as np

height = 0.2
p = np.arange(len(x))
p1 = [j + height for j in p]


plt.barh(p, y, height, color = c, label = "Popularity")
plt.barh(p1, z, height, color = "r", label = "Interest")

plt.yticks(p + height/2 , x, rotation = 10) # rotation is optional
plt.legend()
plt.show()
