'''def greeting(uname):
    p1 = "John" #becomes your local variable
    print ("Hello there")

p2 = "Alex" #becomes your global variable

print(p1) #cannot access local variables
print(p2) # can only print global variables'''

# Class -- Cat

class Cat: 
    
    cat = "feline"
    #constructor
    def __init__(self,cname,color,weight,breed):
        self.cname = cname
        self.color = color
        self.weight = weight
        self.breed = breed

    #new function : purpose: Just to print the cats details
    def printCatDetails(self):
        print("----------Cat's details --------")
        print("Name: ", self.cname)
        print("Color: ", self.color)
        print("Weight: ", self.weight, " in kg")
        print("Breed: ", self.breed)

usercname = str(input("Hi, please answer the following questions: \nCat's name: "))
usercolor = str(input("Cat's color? "))
userweight = str(input("Cat's weight in kg? "))
userbreed = str(input("Cat's breed? "))

#create the object. # obj = class (input)
mycat = Cat (usercname, usercolor, userweight, userbreed)

#use object
mycat.printCatDetails()