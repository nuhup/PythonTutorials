
#Evaluate grade avg
threshold_a = 2.7

#complex/nested data structure
students = [
  {
    "grades": [1, 3, 4],
    "name": "John",
    "surname": "Wick"
  },
  {
    "grades": [2, 5, 3],
    "name": "Tom",
    "surname": "Cruise"
  }
]

for student in students:
  #print(student)
  print("Student name:", student["name"], student["surname"])

  totalSum = 0
  for grade in student["grades"]:
    totalSum = totalSum + grade

  avgGrade = totalSum / len(student["grades"])
  print("average grade:", avgGrade)

  if avgGrade <= threshold_a:
    print(student["name"], student["surname"], "passed")
  else:
    print(student["name"], student["surname"], "failed")

  threshold_b = 2.5
  if avgGrade >= threshold_b and avgGrade <= threshold_a:
    print("inform parents about grade")
