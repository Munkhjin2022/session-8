sprice=0.0
sum=0.0

def compt(make,vcode,msrp,model):

  newmsrp=msrp-msrp*discount

  t=newmsrp+(newmsrp*0.07)

  return t

response=input("Do you want to continue? Yes or No")
while(response=="Yes"):
  make=str(input("Enter make of the car "))
  vcode=str(input("Enter vehicle code (Yes or No) "))
  msrp=float(input("Enter sticker price of the automobile "))
  model=str(input("Enter model of the car "))

  if make=="Honda" and model=="Accord":
    discount=0.10
  elif make=="Toyata" and model=="Rav4":
    discount=0.15
  elif make=="electric":
    discount=0.30
  else:
    discount=0.05
  
  t=compt(make, vcode, msrp, model)

  print("Total is: ", float(t))
  response=input("Do you want to continue? Yes or No ")

sum=sum(t)