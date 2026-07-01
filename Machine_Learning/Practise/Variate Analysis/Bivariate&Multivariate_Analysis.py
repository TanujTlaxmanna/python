import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips') # This is a built in dataset
print(tips.head())

titanic = pd.read_csv("csv's\\titanic.csv")
print(titanic.head())

flights = sns.load_dataset('flights')
print(flights.head())

iris = sns.load_dataset('iris')
print(iris.head())


# SCATTER PLOT 

# Bivariate
sns.scatterplot(x = 'total_bill', y = 'tip', data = tips, palette=['red', 'blue'])
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.savefig("EDA Graphs\\Bivariate\\Scatter_Bivariate.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

# Multivariate
# Scatter Plot (Hue)
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex', palette=['red', 'blue'])
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.savefig("EDA Graphs\\Multivariate\\Scatter_Hue.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

# Scatter Plot (Hue + Style)
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex', palette=['red', 'blue'], style='smoker')
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.savefig("EDA Graphs\\Multivariate\\Scatter_Hue_Style.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

# Scatter Plot (Hue + Style + Size)
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex', palette=['red', 'blue'], style='smoker', size='size')
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.savefig("EDA Graphs\\Multivariate\\Scatter_Hue_Style_Size.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()


# BARPLOT 

# BIVARIATE 
sns.barplot(x = 'Pclass', y = 'Age', data = titanic, palette = ['b', 'g', 'orange'])
plt.title("Average Age by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Age")
plt.savefig("EDA Graphs\\Bivariate\\Barplot_titanic_Age.png", dpi = 300, facecolor = 'lightpink', transparent = True, bbox_inches = "tight")
plt.show()

sns.barplot(x = 'Pclass', y = 'Fare', data = titanic, palette = ['b', 'g', 'orange'])
plt.title("Average Fare by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Age")
plt.savefig("EDA Graphs\\Bivariate\\Barplot_titanic_Fare.png", dpi = 300, facecolor = 'lightpink', transparent = True, bbox_inches = "tight")
plt.show()


# MULTIVARIATE
sns.barplot(x = 'Pclass', y = 'Age', data = titanic, palette = ['b', 'g', 'orange'], hue = 'Sex')
plt.title("Average Age by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Age")
plt.savefig("EDA Graphs\\Multivariate\\Barplot_Pclass_Age_Sex.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

sns.barplot(x = 'Pclass', y = 'Fare', data = titanic, palette = ['b', 'g', 'orange'], hue = 'Sex')
plt.title("Average Fare by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Age")
plt.savefig("EDA Graphs\\Multivariate\\Barplot_Pclass_Fare_Sex.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()


# BOXPLOT 

# BIVARIATE 
sns.boxplot(x='Sex', y='Age', data=titanic, palette=['red', 'blue'])
plt.title("Age Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Age")
plt.savefig("EDA Graphs\\Bivariate\\Boxplot_Sex_Age.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()


# MULTIVARIATE 
sns.boxplot(x='Sex', y='Age', data=titanic, hue='Survived', palette=['red', 'green'])
plt.title("Age Distribution by Gender and Survival")
plt.xlabel("Gender")
plt.ylabel("Age")
plt.savefig("EDA Graphs\\Multivariate\\Boxplot_Sex_Age_Survived.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()


# DISTPLOT
sns.kdeplot(data=titanic[titanic['Survived'] == 0], x='Age', color='red', label='Did Not Survive')
sns.kdeplot(data=titanic[titanic['Survived'] == 1], x='Age', color='green', label='Survived')
plt.title("Age Distribution by Survival Status")
plt.xlabel("Age")
plt.ylabel("Density")
plt.legend()
plt.savefig("EDA Graphs\\Multivariate\\Distplot_Age_Survived.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()


# HEATMAP 
print(titanic.head(3))

a = pd.crosstab(titanic['Pclass'], titanic['Survived'])
print(a)
sns.heatmap(a, annot=True, cmap='Blues', fmt='.0f')
plt.title("Heatmap of Passenger Class vs Survival")
plt.xlabel("Survival Status")
plt.ylabel("Passenger Class")
plt.savefig("EDA Graphs\\Multivariate\\Heatmap_Pclass_Survived.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

(titanic.groupby('Pclass').mean(numeric_only=True)['Survived'] * 100).plot(kind='bar', color=['red', 'green', 'blue'])
plt.title("Survival Percentage by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Percentage (%)")
plt.savefig("EDA Graphs\\Multivariate\\Barplot_Survival_Percentage_Pclass.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

(titanic.groupby('Sex').mean(numeric_only=True)['Survived'] * 100).plot(kind='bar', color=['red', 'green'])
plt.title("Survival Percentage by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Percentage (%)")
plt.savefig("EDA Graphs\\Multivariate\\Barplot_Survival_Percentage_Sex.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

(titanic.groupby('Embarked').mean(numeric_only=True)['Survived'] * 100).plot(kind='bar', color=['red', 'green', 'blue'])
plt.title("Survival Percentage by Embarkation Port")
plt.xlabel("Embarkation Port")
plt.ylabel("Survival Percentage (%)")
plt.savefig("EDA Graphs\\Multivariate\\Barplot_Survival_Percentage_Embarked.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

sns.heatmap(flights.pivot_table(values='passengers', index='month', columns='year'), annot=True, fmt='.0f', cmap='Blues')
plt.title("Monthly Passenger Count Heatmap")
plt.xlabel("Year")
plt.ylabel("Month")
plt.savefig("EDA Graphs\\Bivariate\\Heatmap_Flights.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()


# CLUSTER MAP 

# CLUSTERMAP OF PARENTS/CHILDREN VS SURVIVAL
c = pd.crosstab(titanic['Parch'], titanic['Survived'])
print(c)
g = sns.clustermap(c, annot=True, cmap='Blues', fmt='.0f')
g.savefig("EDA Graphs\\Multivariate\\Clustermap_Parch_Survived.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()



g = sns.clustermap(flights.pivot_table(values='passengers', index='month', columns='year'), annot=True, fmt='.0f', cmap='Blues')
g.savefig("EDA Graphs\\Multivariate\\Clustermap_Flights.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

# PAIRPLOT  THIS IS A COLLECTION OF SCATTER PLOT

# BIVARIATE 
print(iris.head())
sns.pairplot(iris)
plt.savefig("EDA Graphs\\Bivariate\\Pairplot_Iris.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

# MULTIVARIATE 
# PAIRPLOT WITH SPECIES
print(iris.head())
g = sns.pairplot(iris, hue='species')
g.savefig("EDA Graphs\\Multivariate\\Pairplot_Iris_Species.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

# LINE PLOT  (JOIN ALL SCATTER PLOT POINTS TO GETHER, TIME DATA)
# LINE PLOT
print(flights.head())

# LINE PLOT

new = flights.groupby('year')['passengers'].sum().reset_index()
print(new)
sns.lineplot(x='year', y='passengers', data=new)
plt.title("Total Passengers by Year")
plt.xlabel("Year")
plt.ylabel("Number of Passengers")
plt.savefig("EDA Graphs\\Bivariate\\Lineplot_Passengers_Year.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()