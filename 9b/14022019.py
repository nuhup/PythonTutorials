incoming_numbers = [1, 345, 20, 34, 234]

#inside
for num in incoming_numbers:
  if num >= -23 and num < 57:
    print(num)

#outside
for num in incoming_numbers:
  if num > 57 or num <= -23:
    print(num)
