def compsq(l, w, h):
  sq=(2*l*w)+(2*l*h)+(2*w*h)
  return sq

def compg(sq):
  g=sq/50
  return g

val=input("Do you want to continue? Da or Nyet")
while(val=="Da"):
  l=float(input("Enter length of the room"))
  w=float(input("Enter width of the room"))
  h=float(input("Enter height of the room "))
  sq=compsq(l,w,h)
  g=compg(sq)
  print("Number of gallons needed: " + str(g))
  val=input("Do you want to continue? Da or Nyet")