amt=int(input("enter the billing amount: "))
location=str(input("enter the location: "))

if(location.upper()=="BANGALORE" or location.upper()=="BENGALURU"):
    if(amt>=500):
        print("free shipping :)")
    else:
        print("shipping cost is 49 only :)")
else:
    if(amt>=500):
        print("shipping cost is 99 only :)")
    elif(amt>=300):
        print("shipping cost is 149 only :)")
    else:
        print("shipping charge is 199 only :)")
print("Thanks for shopping...")