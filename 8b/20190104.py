students = [{
    "grades": [1, 3, 4],
    "name": "John",
    "surname": "Wick"
}, {
    "grades": [2, 5, 3],
    "name": "Tom",
    "surname": "Cruise"
}]

#solution without avg function def
for student in students:
  sum_grades = 0
  num_grades = len(student["grades"])
  for grade in student["grades"]:
      sum_grades = sum_grades + grade
  print(sum_grades/num_grades)

#solution with avg function def
def avg(numbers):
  sum_num = 0
  len_num = len(numbers)
  for num in numbers:
      sum_num = sum_num + num
  return sum_num/len_num

for student in students:
  print( avg(student["grades"]) )
