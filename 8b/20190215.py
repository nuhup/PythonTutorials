#Automatic Test Review

#Simple variable
threshold = 15 #min result to pass

#Complex Variable - Dictionary
#This data-structure is called dictionary.
#Allows us to store multiple data in one single variable.
student = {
  "result": 18,
  "name": "Tom",
  "surname": "Cruise"
}

if student["result"] >= threshold:
  print(student["name"], student["surname"], "passed")
else:
  print(student["name"], student["surname"], "failed")
