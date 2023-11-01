#create a distance converter function

'''def distConverter(metres): 
    dist = metres / 1000
    print ("distance is: "+ str(dist) + "km")'''

def distConverter ():
    Choice = int (input ("Enter 1 for m to km \nEnter 2 for km to m \n"))
    if Choice==1: 
        dist = int(input("Enter distance in metres: "))
        ans = dist/1000
        print("distance is: " + str(ans) + " km")
    
    elif Choice==2: 
        dist2 = int(input("Enter distance in km: "))
        ans2 = dist2 * 1000
        print ("distance is: " + str(ans2) + "metre")
    
    else: 
        print ("Sorry, wrong choice. Please select 1 or 2")

#Call the function
#distConverter()

    
#call the function
'''distConverter (500)'''

#distConverter() #Output: Enter distance in metres


#Exercise 1: 
def nameage (name, age):
    print("Hi " + name)
    print ("Your age is: " + str (age))

#call this function
#nameage ("Betty", 21)
#Output: Hi Betty, Your age is: 21

#Exercise 2: 
def calculation (a, b):
    ans = a + b
    print(ans)

#result = calculation (10, 15)
# Output: 25
