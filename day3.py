students = [
{"name": "Joe", "score":20},
{"name": "Dwayne", "score":19},
{"name": "Bjorn", "score":15}]

#for student in students:
  #print(f"{student['name']} Score {student['score']} ")

name = "juan dela cruz "

print(name.strip())
print(name.upper())
print(name.lower())
print(name.title().strip())
print(name.replace("juan", "jose"))

sentence = "J Dea Cuz"
words = sentence.split()

print(words)
print(words[0])
print(words[-1])


date = "2024-05-24"

#parts = date.split("-")

#print(parts)
#print(f"Year: {parts[0]}, Month: {parts[1]}, Day: {parts[2]}")

#students = "Juan, Maria, Jose, Ana"
#parts = students.split(",")

#for student in parts:
  #print(f"{student.strip().title()}")

file = open("student.csv", "r")
lines = file.readlines()
file.close()



for line in lines[1:]:
  parts = line.strip().split(",")

  student = {
    "name": parts[0],
    "age": parts[1],
    "grade": parts[2]
  }

  grade = int(student['grade'])

  if grade >= 90:
    label = "Excellent"
  elif grade >=80:
    label = "Good"
  else:
    label = "Needs Improvement"
    
  print(f"Name: {student['name']}, Age:{student['age']}, Score:{int(student['grade']) }- {label}")
