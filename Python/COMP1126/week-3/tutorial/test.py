OVER10LBSNL = 3.80
OVER10LBSINTL = 4.50
OVER6LBS = 3.70
OVER2LBS = 2.20
LESSTHAN2LBS = 1.10
NATIONAL = "National"
INTERNATIONAL = "International"


def destinationPrompt():
  
  destination = input("Where is the package being shipped: ")
  while (destination not in (NATIONAL.lower(), INTERNATIONAL.lower(), NATIONAL, INTERNATIONAL)):
     print("Invalid destination. Please enter either 'National' or 'International'.")
     destination = input("Where is the package being shipped: ")

  return "N" if destination in (NATIONAL.lower(), NATIONAL) else "I"


def weightPrompt():
  
  weight = int(input("What is the weight of the package: "))
  return weight


def shipping_charges(weight, destination):
  
  if weight <= 2:
        price = LESSTHAN2LBS * weight
  elif 2 < weight <= 6:
      price = OVER2LBS * weight
  elif 6 < weight <= 10:
      price = OVER6LBS * weight
  elif weight > 10 and destination == "I":
      price = OVER10LBSINTL * weight
  elif weight > 10 and destination == "N":
      price = OVER10LBSNL * weight
  else:
    return "Unable to calculate the price"
    
  return price
    

  
  
destination = destinationPrompt()
weight = weightPrompt()
print(shipping_charges(weight, destination))


# def smallest(x, y, z):
  
#   return min(x,y,z)

# print(smallest(10, 2, 100))


# FIVEUNITDISCOUNT = 0.10
# TENUNITDISCOUNT = 0.125

# def salesTotal(price, units):
#   if(units <= 5):
#     price = price
#   elif ( 5 < units <= 10):
#     price = price - (price * FIVEUNITDISCOUNT) 
#   elif (units > 10 ):
#     price = price - (price * TENUNITDISCOUNT) 
#   else:
#     return "Unable to calculate the total"
  
#   return price


# print(salesTotal(100, 12))
  

# def fivePowers(base):
  
#   exponent = 0
#   results = []
#   while (exponent <= 4):
#     result = base**exponent
#     results.append(result)
#     exponent += 1
    
#   return results


# print(fivePowers(3))


# def power_list(base, numberOfPowers):
  
#   exponent = 0
#   results = []
#   while (exponent <= numberOfPowers):
#     result = base ** exponent
#     results.append(result)
#     exponent += 1
#   return results

# print(power_list(3,10))
  


def salarycalculator(days):
  
  day = 1
  totalPay = 2 ** days-1
  
  while(day <= days):
    salary = 2**(day-1)
    print(f"The salary for day {day} is ${salary}")
    day += 1
  
  return f"The total pay for {days} days is {totalPay}"
    
  

# print(salarycalculator(5))


# def absoluteValue(x,y,z):

#   return (abs(x ) + abs(y) + abs(z))/3
  
# print(absoluteValue(2, 4, 6))
# print(absoluteValue(-2, 4, 6))
# print(absoluteValue(63, -55, -134))


def shipping_charges(weight, destination):
  
  if weight <= 2:
    price = 1.10 * weight
  elif 2 < weight <= 6:
    price = 2.20 * weight
  elif 6 < weight <= 10:
    price = 3.70 * weight
  elif weight > 10:
    if destination == "N":   
      price = 3.80 * weight
    else:
      price = 4.50 * weight
  else:
    return "Unable to calculate the price"
  
  return price