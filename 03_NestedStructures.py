collection = [
  {"student": "Filippo", "grade": 3},
  {"student": "Giada", "grade": 6},
  {"student": "Salvatore", "grade": 2},
  {"student": "Chris", "grade": 2},
  {"student": "Naomi", "grade": 4},
  {"student": "Moira", "grade": 3},
  {"student": "Doug", "grade": 3},
]

#Evaluate AVG
grade_sum = 0
for elem in collection:
  grade_sum = grade_sum + elem["grade"]

grade_avg = grade_sum / len(collection)
print("AVG:", grade_avg)

#Evaluate MAX (1 - Maximum, 6 - Minimum)
grade_max = 6
for elem in collection:
  incoming_grade = elem["grade"]
  if incoming_grade < grade_max:
    grade_max = incoming_grade

print("MAX:", grade_max) 

#Evaluate MIN (1 - Maximum, 6 - Minimum)
grade_min = 1
for elem in collection:
  incoming_grade = elem["grade"]
  if incoming_grade > grade_min:
    grade_min = incoming_grade
    
print("MIN:", grade_min) 

