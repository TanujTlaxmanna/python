import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("csv's\\titanic.csv")
print(df.head())

# CATEGORICAL DATA 

# COUNTPLOT 
print(df['Survived'].value_counts())
sns.countplot(x = 'Survived', data = df, palette=['red', 'green'], hue='Survived', legend = True)
plt.legend(labels=['Dead', 'Survived'])
plt.savefig("EDA Graphs\\Survived_count.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

print(df['Pclass'].value_counts())
sns.countplot(x = 'Pclass', data = df, palette=['red', 'green', 'blue'], hue='Pclass', legend = True)
plt.legend(labels = ['First Class', 'Second Class', 'Third Class'])
plt.savefig("EDA Graphs\\Pclass_count.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

print(df['Sex'].value_counts())
sns.countplot(x = 'Sex', data = df, palette=['red', 'green'], hue='Sex', legend = True)
plt.legend(labels=['Male', 'Female'])
plt.savefig("EDA Graphs\\Sex_count.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

print(df['Embarked'].value_counts())
sns.countplot(x = 'Embarked', data = df, palette=['red', 'green', 'blue'], hue='Embarked', legend = True)
plt.legend(labels = ['Cherbourg', 'Queenstown', 'Southampton'])
plt.savefig("EDA Graphs\\Embarked_count.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()



# PIE CHART 
# Survived
df['Survived'].value_counts().plot(kind='pie', autopct='%.2f%%')
plt.title("Survival Distribution")
plt.ylabel("")
plt.savefig("EDA Graphs\\Survived_pie.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

# Passenger Class
df['Pclass'].value_counts().plot(kind='pie', autopct='%.2f%%')
plt.title("Passenger Class Distribution")
plt.ylabel("")
plt.savefig("EDA Graphs\\Pclass_pie.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

# Sex
df['Sex'].value_counts().plot(kind='pie', autopct='%.2f%%')
plt.title("Gender Distribution")
plt.ylabel("")
plt.savefig("EDA Graphs\\Sex_pie.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

# Embarked
df['Embarked'].value_counts().plot(kind='pie', autopct='%.2f%%')
plt.title("Embarkation Port Distribution")
plt.ylabel("")
plt.savefig("EDA Graphs\\Embarked_pie.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()


# NUMERICAL DATA 

#HISTOGRAM
print(df['Age'].value_counts())
plt.hist(df['Age'], bins = 5)
plt.savefig("EDA Graphs\\Age_Histo.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()

# DISTPLOT (removed from newer seabord versions, kde is kernal destribution estimation(the line curve))
sns.histplot(df['Age'], kde=True, color='royalblue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig("EDA Graphs\\Age_histplot.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()


# BOXPLOT 
sns.boxplot(x=df['Fare'])
plt.title("Fare Box Plot")
plt.xlabel("Fare")
plt.savefig("EDA Graphs\\Fare_boxplot.png", dpi=300, facecolor='lightpink', transparent=True, bbox_inches="tight")
plt.show()