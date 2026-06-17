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

# import numpy as np

# # x = np.array([3,8,7,4,5,7,0,9,1,2,3,4,7,4])
# y = np.array([1,2,3,4,5,2,8,9,3,6,1,9,4,9])
# # plt.plot(x)
# plt.plot(y)  # Plotting graph with default color and line style
# plt.show()

# plt.plot(y, color = "red") # Plotting graph with red line
# plt.show()

# plt.plot(y, color = "red", linestyle = "dashed") # Plotting graph with red dashed line
# plt.show()

# plt.plot(y, color = "red", linestyle = "dashed", linewidth = 5) # Plotting graph with red dashed line and bigger line width 
# plt.show()

# plt.plot(y, color = "red", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "blue", markeredgecolor = "black", markersize = 10) # Plotting graph with red dashed line and bigger line width and markers
# plt.show()

# plt.plot(y, color = "red", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "blue", markeredgecolor = "black", markersize = 10, alpha = 0.5) # Plotting graph with red dashed line and bigger line width and markers and transparency
# plt.show()


# MULTIPLE LINE GRAPHS

# y = np.array([1,2,3,4,5,2,8,9,3,6,1,9,4,9])
# y1 = np.array([3,8,7,4,5,7,0,9,1,2,3,4,7,4])

# plt.plot(y, color = "red", linestyle = "dashed", linewidth = 2, marker = "o", markerfacecolor = "blue", markeredgecolor = "black", markersize = 10, alpha = 0.5, label = "Line 1") # Plotting graph with red dashed line and bigger line width and markers and transparency
# plt.plot(y1, color = "green", linestyle = "solid", linewidth = 2, marker = "s", markerfacecolor = "yellow", markeredgecolor = "black", markersize = 10, alpha = 0.5, label = "Line 2") # Plotting graph with green solid line and bigger line width and markers and transparency
# plt.legend(["women", "men"]) # Adding legend to the graph
# plt.show()

# ---------------------------------------------------------------
#  HISTOGRAM PLOT
# ---------------------------------------------------------------


# SYNTAX:
# x = []
# plt.hist(x)
# plt.show()

# import numpy as np
# import random

# x = np.random.randint(10, 60, 50)
# print(x) 

# number = [41, 36, 21, 41, 42, 31, 37, 39, 15, 20, 26, 12, 10, 44, 45, 14, 23, 42, 55, 42, 53, 58, 40, 54,
#           55, 46, 31, 41, 45, 48, 29, 24, 33, 11, 19, 50, 15, 27, 42, 14, 55, 36, 38, 55, 39, 45, 38, 26,
#           58, 27]
# bins = [10,20,30,40,50,60]

# plt.title("Histogram Plot", fontsize = 15)
# plt.xlabel("Python", fontsize = 15)
# plt.ylabel("Numbers", fontsize = 15)

# plt.hist(number)  # Plotting the histogram with default number of bins
# plt.show()

# plt.hist(number, color = "r") # Plotting the histogram with red color 
# plt.show()

# plt.hist(number, color = "r", edgecolor = "black") # Plotting the histogram with red color and black edge color
# plt.show()

# plt.hist(number, color = "r", bins = bins, edgecolor = "black") # Plotting the histogram with red color, custom bins and black edge color
# plt.show()

# plt.hist(number, color = "r", bins = "auto", range = (0,100),  edgecolor = "black") # Plotting the histogram with red color, automatic bins, custom range and black edge color
# plt.show()

# plt.hist(number, color = "r", edgecolor = "black", cumulative = -1) # Plotting the histogram with red color, black edge color and cumulative histogram, cumulative = -1 will plot the cumulative histogram in reverse order
# plt.show()

# plt.hist(number, color = "r", edgecolor = "black", bottom = 10) # Plotting the histogram with bottom as 10 this will start the y axis with 10
# plt.show()

# plt.hist(number, color = "r", edgecolor = "black", align = "left") # Plotting the histogram with left alignment, this is bydefault
# plt.show()

# plt.hist(number, color = "r", edgecolor = "black", histtype = "step") # Plotting the histogram with step type, this will plot the histogram as a step function
# plt.show()

# plt.hist(number, color = "r", edgecolor = "black", orientation = "horizontal") # Plotting the histogram with horizontal orientation, by default vertical
# plt.show()

# plt.hist(number, color = "r", edgecolor = "black", rwidth = 0.5) # Plotting the histogram with relative width of the bars, this will make the bars thinner
# plt.show()

# plt.hist(number, color = "r", edgecolor = "black", log = True) # Plotting the histogram with logarithmic scale, this will make the y axis logarithmic
# plt.show()

# plt.hist(number, color = "r", edgecolor = "black", label = "Pythons")
# plt.legend() # Adding legend to the histogram
# plt.show()

# plt.hist(number, color = "r", edgecolor = "black", label = "Pyhtodns")
# plt.axvline(45, color = "b", linestyle = "dashed", linewidth = 2, label = "Mean") # Adding a vertical line to the histogram at x = 45
# plt.legend()
# plt.show()



# ---------------------------------------------------------------
#  PIE  PLOT
# ---------------------------------------------------------------


# SYNTAX:
# x = []
# plt.pie(x)
# plt.show()


# x = [10,20,30,40]
# y = ["python", "c", "c++", "java"]
# ex = [0.0, 0.2, 0.0, 0.0] # explode will separate the slices of the pie chart, this is bydefault 0.0 for all slices
# c = ['r', 'g', 'b', 'y']
# plt.title("Pie Chart", fontsize = 15) # Adding title to the pie chart

# plt.pie(x) # Plotting basic pie chart
# plt.show()


# plt.pie(x, labels = y) # Plotting pie chart with labels
# plt.show()

# plt.pie(x, labels = y, colors = c, explode = ex) # Plotting labels with colors and explode
# plt.show()

# plt.pie(x, labels = y, colors = c, explode = ex, autopct = "%1.1f%%") # Plotting pie chart with labels and percentage
# plt.show() 

# plt.pie(x, labels = y, colors = c, explode = ex, autopct = "%1.1f%%", shadow = True) # Plotting pie chart with labels and percentage and shadow
# plt.show() 

# plt.pie(x, labels = y, colors = c, explode = ex, autopct = "%1.1f%%", shadow = True, radius = 1) # Plotting pie chart with labels and percentage and shadow and bigger radius
# plt.show() 

# plt.pie(x, labels = y, colors = c, explode = ex, autopct = "%1.1f%%", shadow = True, radius = 1, labeldistance = 1.1) # Plotting pie chart with labels and percentage and shadow and start angle and label distance
# plt.show() 

# plt.pie(x, labels = y, colors = c, explode = ex, autopct = "%1.1f%%", shadow = True, radius = 1, labeldistance = 1.1, startangle = 90) # Plotting pie chart with labels and percentage and shadow and start angle and label distance
# plt.show() 

# plt.pie(x, labels = y, colors = c, explode = ex, autopct = "%1.1f%%", shadow = True, radius = 1, labeldistance = 1.1, startangle = 90, textprops = {'fontsize': 10}) # Plotting pie chart with labels and percentage and shadow and start angle and label distance and bigger font size
# plt.show() 

# plt.pie(x, labels = y, colors = c, explode = ex, autopct = "%1.1f%%", shadow = True, radius = 1, labeldistance = 1.1, startangle = 90, textprops = {'fontsize': 10}, counterclock = False) # Plotting pie chart with labels and percentage and shadow and start angle and label distance and bigger font size and counterclockwise
# plt.show() 

# plt.pie(x, labels = y, colors = c, explode = ex, autopct = "%1.1f%%", shadow = True, radius = 1, labeldistance = 1.1, startangle = 90, textprops = {'fontsize': 10}, counterclock = False, wedgeprops = {'linewidth': 2, 'edgecolor': 'white'}) # Plotting pie chart with labels and percentage and shadow and start angle and label distance and bigger font size and counterclockwise
# plt.show() 

# plt.pie(x, labels = y, colors = c, explode = ex, autopct = "%1.1f%%", shadow = True, radius = 1, labeldistance = 1.1, startangle = 90, textprops = {'fontsize': 10}, counterclock = False, wedgeprops = {'linewidth': 2, 'edgecolor': 'white'}, center = (2,3)) # Plotting pie chart with labels and percentage and shadow and start angle and label distance and bigger font size and counterclockwise and bigger wedge width and edge color and center
# plt.show()

# plt.pie(x, labels = y, colors = c, explode = ex, autopct = "%1.1f%%", shadow = True, radius = 1, labeldistance = 1.1, startangle = 90, textprops = {'fontsize': 10}, counterclock = False, wedgeprops = {'linewidth': 2, 'edgecolor': 'white'}, center = (2,3), rotatelabels = True) # Plotting pie chart with labels and percentage and shadow and start angle and label distance and bigger font size and counterclockwise and bigger wedge width and edge color and center and rotate labels
# plt.legend(loc = 2) # Adding legend to the pie chart, loc = 2 will place the legend at the upper left corner, Quadrant based 1,2,3,4
# plt.show()


# DOT PIE CHART

# plt.pie([1]) 
# plt.show()

# DONUT PIE CHART 


# x = [10,20,30,40]
# x1 = [40,30,20,10]
# y = ["python", "c", "c++", "java"]
# c = ['r', 'g', 'b', 'y']
# plt.title("Pie Chart", fontsize = 15)

# plt.pie(x, labels = y, radius = 1.5)
# plt.pie(x1, radius = 0.5, colors = c)
# plt.show()


# plt.pie(x, labels = y, radius = 1.5)
# plt.pie([1], colors = 'w') # Adding a white circle in the middle to create a donut chart ,instead of radius we can do [1] in the start of code
# plt.show()


# SECOND METHOD FOR DONUT


# plt.pie(x, labels = y, radius = 1.5)
# cr = plt.Circle((0,0), 0.5, facecolor = "white") # Creating a white circle with radius 0.5
# plt.gca().add_artist(cr)

# plt.show()


# ---------------------------------------------------------------
#  STEM PLOT
# ---------------------------------------------------------------


# SYNTAX:
# x = []
# y = []
# plt.stem(x, y)
# plt.show()

# x = [1,2,3,4,5,6]
# y = [2,4,6,8,10,12]

# plt.stem(x, y) # Plotting the stem plot with default line style and marker
# plt.show()

# plt.stem(x, y, linefmt = ":") # Plotting the stem plot with dotted line 
# plt.show()

# plt.stem(x, y, linefmt = ":", markerfmt = "o") # Plotting the stem plot with dotted line and circle marker and symbol
# plt.show()

# plt.stem(x, y, linefmt = ":", markerfmt = "o", bottom = 4) # Plotting the stem plot with dotted line and circle marker and symbol and bottom value)
# plt.show()

# plt.stem(x, y, linefmt = ":", markerfmt = "o", bottom = 4, basefmt = "g") # Plotting the stem plot with dotted line and circle marker and symbol and bottom value and base line color
# plt.show()

# plt.stem(x, y, linefmt = ":", markerfmt = "o", bottom = 4, basefmt = "g", label = "python") # Plotting the stem plot with dotted line and circle marker and symbol and bottom value and base line color and label
# plt.legend()
# plt.show()

# plt.stem(x, y, linefmt = ":", markerfmt = "o", bottom = 4, basefmt = "g", label = "python") # Plotting the stem plot with dotted line and circle marker and symbol and bottom value and base line color and label and use_line_collection however use_line_collection is deprecated and will be removed in a future version
# plt.legend()
# plt.show()

# plt.stem(x, y, linefmt = ":", markerfmt = "o", bottom = 4, basefmt = "g", label = "python", orientation = "horizontal") # Plotting the stem plot with dotted line and circle marker and symbol and bottom value and base line color and label and use_line_collection and horizontal orientation
# plt.legend()
# plt.show()


# ---------------------------------------------------------------
#  BOX PLOT
# ---------------------------------------------------------------


# SYNTAX:
# x = []
# plt.boxplot(x)
# plt.show()

x = [10,20,30,40,50,60,70,80,90,100]

plt.boxplot(x) # Plotting the box plot with default settings
plt.show()

plt.boxplot(x, notch = True) # Plotting the box plot with notch, notch will show the confidence interval of the median
plt.show()

plt.boxplot(x, vert = False) # Plotting the box plot with horizontal orientation, by default vertical
plt.show()

plt.boxplot(x, widths = 0.8) # Plotting the box width with different width (default = 0.2)
plt.show()

plt.boxplot(x, label = ["python"]) # Plotting the box plot with label
plt.legend() # Adding legend to the box plot
plt.show()

plt.boxplot(x, label = ["python"], patch_artist = True) # Plotting the box plot with label and patch artist
plt.legend() # Adding legend to the box plot
plt.show()


plt.boxplot(x, label = ["python"], showmeans = True) # Plotting the box plot with label and patch artist and showing means
plt.legend() # Adding legend to the box plot
plt.show()

x = [10,20,30,40,50,60,70,80,90,100,450]

plt.boxplot(x, label = ["python"], patch_artist = True) 
plt.legend() # Adding legend to the box plot
plt.show()

plt.boxplot(x, label = ["python"], patch_artist = True, whis = 3.6) # Plotting the box plot with label and patch artist and setting the whisker length to 3.6, this will show the outliers as points beyond the whiskers
plt.legend() # Adding legend to the box plot
plt.show()

plt.boxplot(x, label = ["python"], patch_artist = True, showmeans = True, sym = "g+") # Plotting the box plot with label and patch artist and showing means and changing the symbol for outliers to green plus
plt.legend() # Adding legend to the box plot
plt.show()

plt.boxplot(x, label = ["python"], patch_artist = True, showmeans = True, sym = "g+", boxprops = dict(color = "r"), capprops = dict(color = "b")) # Plotting the box plot with label and patch artist and showing means and changing the symbol for outliers to green plus and changing the color of the box to red and the color of the caps to blue
plt.legend() # Adding legend to the box plot
plt.show()

plt.boxplot(x, label = ["python"], patch_artist = True, showmeans = True, sym = "g+", boxprops = dict(color = "r"), capprops = dict(color = "b"), whiskerprops = dict(color = "r")) # Plotting the box plot with label and patch artist and showing means and changing the symbol for outliers to green plus and changing the color of the box to red and the color of the caps to blue and changing the color of the whiskers to red
plt.legend() # Adding legend to the box plot
plt.show()


plt.boxplot(x, label = ["python"], patch_artist = True, showmeans = True, sym = "g+", boxprops = dict(color = "r"), capprops = dict(color = "b"), whiskerprops = dict(color = "r"), flierprops = dict(markeredgecolor = "y")) # Plotting the box plot with label and patch artist and showing means and changing the symbol for outliers to green plus and changing the color of the box to red and the color of the caps to blue and changing the color of the whiskers to red and changing the color of the outliers to yellow
plt.legend() # Adding legend to the box plot
plt.show()


x = [10,20,30,40,50,60,70,80,90,100,450]
x1 = [10,20,30,40,50,60,70,80,90,100,500]
plt.boxplot([x, x1], label = ["python", "python1"], patch_artist = True, showmeans = True, sym = "g+", boxprops = dict(color = "r"), capprops = dict(color = "b"), whiskerprops = dict(color = "r"), flierprops = dict(markeredgecolor = "y")) # Plotting the box plot with label and patch artist and showing means and changing the symbol for outliers to green plus and changing the color of the box to red and the color of the caps to blue and changing the color of the whiskers to red and changing the color of the outliers to yellow
plt.legend() # Adding legend to the box plot
plt.show()

# ---------------------------------------------------------------
#  STEM PLOT
# ---------------------------------------------------------------


# SYNTAX:
# x = []
# y = []
# plt.stem(x, y)
# plt.show()




# ---------------------------------------------------------------
#  STEM PLOT
# ---------------------------------------------------------------


# SYNTAX:
# x = []
# y = []
# plt.stem(x, y)
# plt.show()