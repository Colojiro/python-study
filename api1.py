import pandas as pd
from fastapi import FastAPI
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

app = FastAPI()

# Train the model when the server starts
df = pd.read_csv("train.csv")
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
features = ["Pclass", "Age", "SibSp", "Parch", "Fare", "Sex"]
df = df[features + ["Survived"]]
df["Age"] = df["Age"].fillna(df["Age"].mean())

X = df[features]
y = df["Survived"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

@app.get("/")
def home():
    return {"message": "Titanic Survival Predictor API"}

@app.get("/predict")
def predict(pclass: int, age: float, sibsp: int, parch: int, fare: float, sex: str):
    sex_num = 0 if sex == "male" else 1
    prediction = model.predict([[pclass, age, sibsp, parch, fare, sex_num]])
    result = "Survived" if prediction[0] == 1 else "Did not survive"
    return {"prediction": result}