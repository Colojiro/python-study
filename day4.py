import numpy as np
import pandas as pd

data = {
    "name": ["Juan", "Maria", "Jose", "Ana"],
    "age": [20,19,21,20],
    "grade": [90, 75, 85, 92]
}
numbers = [10, 20, 30, 40, 50]

arr = np.array(numbers)

print(arr)
print(type(arr))
print(arr.mean())
print(arr.sum())
print(arr.max())
print(arr.min())

print(arr + 10)
print(arr * 10)
print(arr > 10)

print(arr[arr > 25])

#df = pd.DataFrame(data)

df = pd.read_csv("student.csv")
print(df)

print(df.describe())
print(df[df["grade"] >= 90])
print(df[df["grade"] >= 85]["name"])

def get_label(grade):
    if(grade >= 90):
        return "Excellent"
    elif grade >= 80:
        return "Good"
    else:
        return "Needs Improvement"
    
df["label"] = df["grade"].apply(get_label)
print(df)
#print(df)

#print(df.head(2))      
#print(df.info())       
#print(df.describe())   


# select one column
#print(df["grade"])

# filter rows
#print(df[df["grade"] >= 85])

