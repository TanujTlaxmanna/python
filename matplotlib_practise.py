import matplotlib.pyplot as plt

# BASICS

# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
# c = ["r", "y", "b", "pink", "g"]

# plt.bar(x, y, color=c)
# plt.show()

# TYPES OF PLOTS

# ---------------------------------------------------------------
# BAR PLOT
# ---------------------------------------------------------------


# SYNTAX:
# x = []
# y = []
# plt.bar(x, y)
# plt.show()

# x = ["python", "c", "c++", "java"]
# y = [85, 70, 60, 82]    
# z = [25, 28, 23, 33]
# plt.xlabel("Languages", fontsize= 15)
# plt.ylabel("Popularity", fontsize = 15)
# plt.title("Popularity of Programming Languages", fontsize = 15)
# c = ["y", "b", "m", "g"]
# plt.bar(x, y, width = 0.5, color = c)
# plt.show()
# plt.bar(x, y, width = 0.5, color = c, align = "edge") # align = "edge" will align the bars to the edge of the x-axis, this is bydefault in center
# plt.show()
# plt.bar(x, y, width = 0.5, color = c, edgecolor = "black", linewidth = 2) # edgecolor will add a border to the bars, linewidth will set the width of the border
# plt.show()
# plt.bar(x, y, width = 0.5, color = c, edgecolor = "black", linewidth = 2, linestyle = ":") # linestyle will set the style of the border, it can be solid, dashed, dotted, dashdot
# plt.show()
# plt.bar(x, y, width = 0.5, color = c, edgecolor = "black", linewidth = 2, hatch = "/") # hatch will add a pattern to the bars
# plt.show()
# plt.bar(x, y, width = 0.5, color = c, edgecolor = "black", linewidth = 2, linestyle = ":", alpha = 0.5) # alpha will set the transparency of the bars, it can be a value between 0 and 1
# plt.show()
# plt.bar(x, y, width = 0.5, color = c, edgecolor = "black", linewidth = 2, linestyle = ":", alpha = 0.5, label = "Popularity") # label will add a label to the bars, it is used in legend
# plt.legend() # legend will show the label of the bars
# plt.show() 

# STACKED BAR GRAPHS

# STACKED ON TOP OF EACH OTHER
# plt.bar(x, y, width = 0.5, color = c, label = "Popularity")
# plt.bar(x, z, width = 0.5, color = "r", label = "Interest")
# plt.legend()
# plt.show()

# STACKED SIDE BY SIDE
# import numpy as np

# width = 0.2
# p = np.arange(len(x))
# p1 = [j + width for j in p]


# plt.bar(p, y, width, color = c, label = "Popularity")
# plt.bar(p1, z, width, color = "r", label = "Interest")

# plt.xticks(p + width/2 , x, rotation = 10) # rotation is optional
# plt.legend()
# plt.show()


# HORIZONTAL BAR GRAPHS
# x = ["python", "c", "c++", "java"]
# y = [85, 70, 60, 82]    
# z = [25, 28, 23, 33]
# plt.xlabel("Languages", fontsize= 15)
# plt.ylabel("Popularity", fontsize = 15)
# plt.title("Popularity of Programming Languages", fontsize = 15)

# plt.barh(x, y, color = "g", label = "Popularity")
# plt.barh(x, z, color = "r", label = "Interest")
# plt.legend()
# plt.show()


# HORIZONTAL STACKED BAR SIDE BY SIDE GRAPHS

# import numpy as np

# height = 0.2
# p = np.arange(len(x))
# p1 = [j + height for j in p]


# plt.barh(p, y, height, color = c, label = "Popularity")
# plt.barh(p1, z, height, color = "r", label = "Interest")

# plt.yticks(p + height/2 , x, rotation = 10) # rotation is optional
# plt.legend()
# plt.show()


# ---------------------------------------------------------------
# SCATTER PLOT
# ---------------------------------------------------------------


# SYNTAX:
# x = []
# y = []
# plt.scatter(x, y)
# plt.show()

# day = [1,2,3,4,5,6,7]
# no = [2,3,4,5,1,2,3]
# colors = ["r", "y", "g", "b", "m", "c", "k"]
# size = [200, 189, 254, 372, 265, 292, 390]
# plt.title("Scatter Plot", fontsize = 15)
# plt.xlabel("Days", fontsize = 15)
# plt.ylabel("Number", fontsize = 15)

# plt.scatter(day, no)  # Plotting the graph with default color and size
# plt.show()

# plt.scatter(day, no, color = colors) # Plotting the graph with different colors for each point
# plt.show()

# plt.scatter(day, no, color = colors, s = size) # Plotting the graph with different colors and sizes for each point  
# plt.show()

# plt.scatter(day, no, color = colors, s = size, alpha = 0.5) # Plotting the graph with different colors, sizes and transparency for each point
# plt.show()

# plt.scatter(day, no, color = colors, s = size, alpha = 0.5, marker = "*") # Plotting the graph with different markers
# plt.show()

# plt.scatter(day, no, color = colors, s = size, alpha = 0.5, marker = "*", edgecolor = "black") # Plotting the graph with different markers and edge color
# plt.show()

# plt.scatter(day, no, color = colors, s = size, alpha = 0.5, marker = "*", edgecolor = "black", linewidths = 2) # Plotting the graph with bigger edgewidth
# plt.show()

# colors = [10, 49, 30, 29, 56, 20, 30]
# plt.scatter(day, no, c = colors, cmap = "viridis", s = size, alpha = 0.5, marker = "*", edgecolor = "black", linewidths = 2) # Plotting the graph with bigger edgewidth
# plt.colorbar() # Adding a color bar to the graph
# plt.show()

# plt.scatter(day, no, c = colors, cmap = "viridis", s = size, alpha = 0.5, marker = "*", edgecolor = "black", linewidths = 2) # Plotting the graph with bigger edgewidth, we use c to pass numeric colors instead of color
# t = plt.colorbar() # Adding a color bar to the graph
# t.set_label("Color Bar", fontsize = 15) # Adding a label to the color bar and fontsize
# plt.show()


# MULTIPLE SCATTER PLOTS 
# day = [1,2,3,4,5,6,7]
# no = [2,3,4,5,1,2,3]
# no2 = [3,4,5,6,7,8,9]
# colors = [10, 49, 30, 29, 56, 20, 30]
# size = [200, 189, 254, 372, 265, 292, 390]
# plt.title("Scatter Plot", fontsize = 15)
# plt.xlabel("Days", fontsize = 15)
# plt.ylabel("Number", fontsize = 15)

# plt.scatter(day, no, c = colors, cmap = "viridis", s = size, alpha = 0.5, edgecolor = "black", linewidths = 2)
# plt.scatter(day, no2, color = "r", s = size, alpha = 0.5, edgecolor = "black", linewidths = 2)
# plt.show()

# ---------------------------------------------------------------
#  LINE PLOT
# ---------------------------------------------------------------


# SYNTAX:
# y = []
# plt.plot(y)
# plt.show()

import numpy as np

# x = np.array([3,8,7,4,5,7,0,9,1,2,3,4,7,4])
y = np.array([1,2,3,4,5,2,8,9,3,6,1,9,4,9])
# plt.plot(x)
plt.plot(y)  # Plotting graph with default color and line style
plt.show()

plt.plot(y, color = "red") # Plotting graph with red line
plt.show()

plt.plot(y, color = "red", linestyle = "dashed") # Plotting graph with red dashed line
plt.show()

plt.plot(y, color = "red", linestyle = "dashed", linewidth = 5) # Plotting graph with red dashed line and bigger line width 
plt.show()

plt.plot(y, color = "red", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "blue", markeredgecolor = "black", markersize = 10) # Plotting graph with red dashed line and bigger line width and markers
plt.show()

plt.plot(y, color = "red", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "blue", markeredgecolor = "black", markersize = 10, alpha = 0.5) # Plotting graph with red dashed line and bigger line width and markers and transparency
plt.show()


# MULTIPLE LINE GRAPHS

y = np.array([1,2,3,4,5,2,8,9,3,6,1,9,4,9])
y1 = np.array([3,8,7,4,5,7,0,9,1,2,3,4,7,4])

plt.plot(y, color = "red", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "blue", markeredgecolor = "black", markersize = 10, alpha = 0.5, label = "Line 1") # Plotting graph with red dashed line and bigger line width and markers and transparency
plt.plot(y1, color = "green", linestyle = "solid", linewidth = 2, marker = "s", markerfacecolor = "yellow", markeredgecolor = "black", markersize = 10, alpha = 0.5, label = "Line 2") # Plotting graph with green solid line and bigger line width and markers and transparency
plt.legend(["women", "men"]) # Adding legend to the graph
plt.show()

# ---------------------------------------------------------------
#  PLOT
# ---------------------------------------------------------------


# SYNTAX:
# x = []
# y = []
# plt.(x, y)
# plt.show()





# ---------------------------------------------------------------
#  PLOT
# ---------------------------------------------------------------


# SYNTAX:
# x = []
# y = []
# plt.(x, y)
# plt.show()




# ---------------------------------------------------------------
#  PLOT
# ---------------------------------------------------------------


# SYNTAX:
# x = []
# y = []
# plt.(x, y)
# plt.show()
