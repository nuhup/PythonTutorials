c = [1, 2, 3, 4, 5, 6]
for num in c: 
  print(num)

d = {
  "name": "Duffy",
  "surname": "Duck"
}
print(d["name"])
name = "Duffy"
print(name)
name = d["name"]
print(name)

data = {
  "temps": [0, 1, 2, 3],
  "location": "Berlin"
}
print(data["location"])

print(data["temps"])
for temp in data["temps"]:
  print(temp)

print([0, 1, 2, 3])
for temp in [0, 1, 2, 3]:
  print(temp)

#------EX 1 - Print a-values times b

data = {
  "a": [1, 2, 3, 4],
  "b": 4
}

for num in data["a"]:
  print((num*data["b"]))


#------EX 2 - Print a-values if major than b

data = {
  "a": [1, 2, 3, 4],
  "b": 4
}


#------EX 3 - Print a-values if minor equal than b

data = {
  "a": [1, 2, 3, 4],
  "b": 4
}


#------EX 4 - Print the b-word if the list a contains "That is"

data = {
  "a": ["boring", "I hate IT", "I love chocolate", "That is"]
  "b": "cool"
}


#------EX 5 - Evaluate average grade for each student
#NOTE: if c is a collection len(c) represent its length (!!)

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




