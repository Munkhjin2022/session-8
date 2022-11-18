t=0.0

def compp(miles):

  return p 

response=input("Do you want to continue? Yes or No ")
while(response=="Yes"):
  name=str(input("Enter the last name "))
  miles=float(input("Enter miles from Downtown Chicago "))

  if miles>=30:
    p=12
  elif miles>=20 and miles<=29:
    p=10
  elif miles>=10 and miles<=19:
    p=8
  else:
    p=5

  p=compp(miles)
  t=t+p

  print("The price: ", float(p))
  response=input("Do you want to continue? Yes or No ")

print("Total: ", float(p))