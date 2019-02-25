#Input Data:
# - Temperature
#our program should just tell us
#when bring a coat: less than 10°

threshold = 10
weatherCondition = {
  "temperature": 9,
  "precipitation": "10%"
  #so on...
}

if weatherCondition["temperature"] <= threshold:
  print ("bring coat")
else:
  print ("don't bring coat")
