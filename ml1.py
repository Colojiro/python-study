import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import matplotlib as plt
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")
#print(df.head())

df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

features = ["Pclass", "Age", "SibSp", "Parch", "Fare","Sex"]
df = df[features + ["Survived"]]

df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df.isnull().sum())

X = df[features]
Y = df["Survived"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print(f"Training rows: {len(X_train)}")
print(f"Testing rows: {len(X_test)}")

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, Y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(Y_test, predictions)

print(f"Accuracy: {accuracy:.2f}")

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(Y_test, predictions)

print(f"Accuracy: {accuracy:.2f}")

importance = pd.Series(model.feature_importances_, index=features)
importance.sort_values().plot(kind="barh", color="skyblue")
plt.title("Feature Importance")
plt.xlabel("Importance")
plt.show()