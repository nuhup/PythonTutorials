#AVG fro colleciton using For-Loop
numbers = [12, 43, 25, 62, 13, 522, 13]

total_sum = 0
for number in numbers:
  total_sum = total_sum + number

print( total_sum / len(numbers) )
