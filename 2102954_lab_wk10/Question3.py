currency = "CSC1009";
def switch(case):
 
  # check if the argument matches the cases
  if case == "AUD":
    print("Australian Dollar")
  elif case == "MYR":
    print ("Malaysian ringgit")
  elif case == "IDR":
    print ("Indonesian Rupiah")
  elif case == "CSC1009":
    print ("Object-Oriented Programming")
  else:
    print ("Unknown Currency")

switch(currency)
print("After Switch")

n=int(102)
if n%2==0:
    for i in range(n-1,66,-2):
        print(i)
else:
    for i in range(n,66,-2):
        print(i)