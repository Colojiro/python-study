import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

print(df.shape)
print(df.head)
print(df.describe())
print(df.isnull().sum())
print(df.groupby("Sex")["Survived"].mean())
"""
survival_by_gender = df.groupby("Sex")["Survived"].mean()
survival_by_gender.plot(kind="bar", color=["coral", "skyblue"])
plt.title("Survival Rate by Gender")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)
plt.show()
"""
'''
survival_by_class =  df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color = ["gold", "silver", "brown"])
plt.title("Survival Rate by Ticket Class")
plt.ylabel("Survival Rate")
plt.xlabel("Class")
plt.xticks(rotation=0)
plt.show()
'''
'''
df["Age"].dropna().hist(bins=20, color="skyblue", edgecolor="black")
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.show()
'''

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Chart 1 - Survival by gender
survival_by_gender = df.groupby("Sex")["Survived"].mean()
axes[0, 0].bar(survival_by_gender.index, survival_by_gender.values, color=["coral", "skyblue"])
axes[0, 0].set_title("Survival Rate by Gender")
axes[0, 0].set_ylabel("Survival Rate")

# Chart 2 - Survival by class
survival_by_class = df.groupby("Pclass")["Survived"].mean()
axes[0, 1].bar(survival_by_class.index, survival_by_class.values, color=["gold", "silver", "brown"])
axes[0, 1].set_title("Survival Rate by Class")
axes[0, 1].set_ylabel("Survival Rate")

# Chart 3 - Age distribution
df["Age"].dropna().hist(bins=20, ax=axes[1, 0], color="skyblue", edgecolor="black")
axes[1, 0].set_title("Age Distribution")
axes[1, 0].set_xlabel("Age")
axes[1, 0].set_ylabel("Count")

# Chart 4 - Overall survival
df["Survived"].value_counts().plot(kind="bar", ax=axes[1, 1], color=["red", "green"])
axes[1, 1].set_title("Overall Survival")
axes[1, 1].set_xticklabels(["Died", "Survived"], rotation=0)

plt.tight_layout()
plt.show()