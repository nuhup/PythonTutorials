#Project Euler #1
#Sum of incoming number, just in case they are multiples of 3 or 5
#Example - 
#   input:
#   3   NOTE: first input is the number of incoming values 'max_count'
#   4
#   5
#   6
#   output:
#   11

max_count = int(input().strip())
tot_sum = 0
counter = 0
while counter < max_count:
  inc_num = int(input().strip())
  if inc_num % 3 == 0 or inc_num % 5 == 0:
    tot_sum = tot_sum + inc_num
  counter = counter + 1
print(tot_sum)
