print("Example 0")
a = [100, 12, 23, 36, 45] 
print(a)

#read a location value
print(a[0])
print(a[2])

#modify a location value
a[1] = 51
print(a) 
a[3] = 345
print(a) 

print(" ")
print("Example 1")

a = [100, 12, 23, 36, 45]
print(  a[2]   ) #23 in console

a = [100, 12, 23, 36, 45]
b = 4
result = a[b]
print(result) #45 in console

a = [100, 12, 23, 36, 45]
b = 1
result = a[b + 1]
print(result) #23 in console


a = [100, 12, 23, 36, 45]
b = 2
result = a[b * 2]
print(result) #45 in console


print(" ")
print("Example 2")

a = [True, False, False]
b = 2
result = a[b-1] and a[b]
result = result or a[b-2]
print(result)

a = [0, 1, 1, 0, 1]
b = 2
result = a[b*2] and a[b]
result = result or a[b+1]
print(result)
