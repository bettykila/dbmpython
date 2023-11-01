#variable year + input function
'''while year ! = 0:
      # IF code comes in  here with the subtraction
      # print the person's age
      # else print wrong value inserted
      break

else: 
    print ("Zero is not a correct year")

print ("Thank you for participating")'''

#Assignment due Tuesday 24/10/2023

def AgeCalculator():
    Year = int(input("Input year: "))
    if input == 0:
        print("Zero is not an accepted input")
    
    elif Year >1800 and Year <2023:
            
        Age = 2023 - Year
        print("Age is " + str(Age))
            
    else: 
        print ("Year is out of bounds. Thank you for participating.")

AgeCalculator ()


    



