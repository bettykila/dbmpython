#creating own exception from Main Exception Class

class OddEvenException (Exception):
    pass

try: 
    userchoice = int(input("Enter number: "))
    if userchoice %2 == 0: 
        print (str(userchoice + " is an EVEN number"))
    
    else:
        print(str(userchoice)+ " is an ODD number")

except: 
    print ("Sorry! Not a valid integer value")