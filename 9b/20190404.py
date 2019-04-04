#Project Euler #1
#1 - Receive N integers numbers.
#2 - Sum all the numbers that repect the condition explained in step 3.
#3 - Keep only the incoming numbers that are multiple of 3 or 5.

print("Receiving N:")
N = int(input()) #number of incoming values

tot_sum = 0
count = 0
while count < N: 
  print("Receiving", count+1, "value :")
  incoming_value = int(input())
  #incoming numnber divisible by 3 or 5
  if incoming_value % 3 == 0 or incoming_value % 5 == 0:            
    tot_sum = tot_sum + incoming_value    #accumulator
  count = count + 1                       #counter

print("Result:", tot_sum)


#Project Euler #1bis (Home Assignment)
#1 - Receive N integers numbers.
#2 - Sum all the numbers that repect the condition explained in step 3.
#3 - Keep only the incoming numbers that are minor tha 255 and major than 0
