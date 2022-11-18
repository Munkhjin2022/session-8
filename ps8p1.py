def compnext(month,sale):
  if(month=="Jan" or month=="Feb" or month=="Mar"):
    p=0.10
  elif(month=="Apr" or month=="May" or month=="Jun"):
    p=0.15
  elif (month=="Jul" or month=="Aug" or month=="Sep"):
    p=0.20
  else:
    p=0.25

  next=sale*(1+p)
  next=round(next, 3)
  return next 

response=input("Do you want to calculate next month sales? Yes or No")

while response=="Yes":
  name=input("Enter the last name ")
  month=input("Enter the month (Jan, Feb, Mar etc)")
  sale=float(input("Enter the sales "))

  next=compnext(month, sale)
  print("Next month sales: ", next)

  response=input("Do you want to calculate month sales? Yes or No")

