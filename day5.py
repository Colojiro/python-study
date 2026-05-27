import matplotlib.pyplot as plt
import pandas as pd

#grades = [90, 75, 85, 92,78]
#names = ["Juan", "Maria", "Jose", "Ana", "Carlos"]

#plt.bar(names, grades, color="coral")
#plt.title("Students Grades")
#plt.xlabel("Students")
#plt.ylabel("Grade")
#plt.show()

#exams = [1,2,3,4,5]
#juan = [70,75,80,78,85]
#maria = [65,70,72,80,88]

#plt.plot(exams, juan, label = "Juan")
#plt.plot(exams, maria, label = "Maria")
#plt.title("Student Progress Over Time")
#plt.xlabel("Exam")
#plt.ylabel("Score")
#plt.xticks(exams)
#plt.grid(True)
#plt.legend()
#plt.show()

df = pd.read_csv("student.csv")

plt.bar(df["name"], df["grade"], color = "skyblue")
plt.title("Student Grades")
plt.xlabel("Students")
plt.ylabel("Grade")

avg = df["grade"].mean()
plt.axhline(y=avg, color="red", linestyle="--", label=f"Average: {avg:.2f}")
plt.legend()
plt.show()

