totalass=0.0
totalmarketval=0.0

def compassessedval(country,marketval):
  assessedval=marketval*assessedpercent

  return assessedval

response=input("Do you want to continue? Yes or No")
while(response=="Yes"):
  county=input("Enter the county")
  marketval=float(input("Enter market value of a home"))

  if (county=="Cook"):
    assessedpercent=0.90
  elif (county=="DuPage"):
    assessedpercent=0.80
  elif (county=="McHenry"):
    assessedpercent=0.75
  elif (county=="Kane"):
    assessedpercent=0.60
  else:
    assessedpercent=0.70
  
  totalmarketval=totalmarketval+marketval
  totalass= totalass+compassessedval(county,marketval)
 
  print("Total market values:",totalmarketval)
 
  print("Total assessef values: ",totalass)