#Control Structures 1 - IF Statement

#EX 1
#Bank Transaction

#Variables Received From Payment System
account = 7000
price = 150

#solution
if account >= price:
  account = account - price
  print("Transaction Accepted") #I have enough money
else:
  print("Transaction Denied") #I don´t have enough money
  
  
#EX 2
#Automatic Car Key

#Variables Received From Car System
#distance in meters
car_ds = 10
#Emergency Block from smartphone
e_block = False

#solution 1
if car_ds <= 10 and e_block == False :
  print("open car")
else:
  print("keep the car closed")

#solution 2
if car_ds <= 10 and not e_block:
  print("open car")
else:
  print("keep the car closed")

#solution 3 NESTED-IFs
if car_ds <= 10:
  if e_block == False:
    print("open car")
  else:
    print("keep the car closed")

#solution 4 NESTED-IFs
if car_ds <= 10:
  if not e_block:
    print("open car")
  else:
    print("keep the car closed")




