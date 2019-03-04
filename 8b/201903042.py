#Automatic Average Calculator
threshold_a = 2.7 #min grade to pass the year
student = {
  "grade1": 2.9,
  "grade2": 2.5,
  "name": "Tom",
  "surname": "Cruise"
}

#avrage grade
avgGrade = student["grade1"] + student["grade2"]
avgGrade = avgGrade/2
print(avgGrade)

if avgGrade <= threshold_a:
  print(student["name"], student["surname"], "passed")
else:
  print(student["name"], student["surname"], "failed")

#Warning Message: call parents in case grade is between 2.7 - 2.5
threshold_b = 2.5
if avgGrade >= threshold_b and avgGrade <= threshold_a:
  print("call the parents")
