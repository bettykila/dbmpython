#Create class Rectangle
class Rectangle: 

    #create constructor
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def RectPeri(self):
        print ("Perimeter is: ", (self.length * self.width), " cm2")

Userlength = int(input("Enter length (cm): "))
Userwidth = int(input("Enter Width (cm): "))

#object instantiation . Attach to class only with parameters
RectObj = Rectangle (Userlength, Userwidth)

#use the object created. Call function here.
RectObj.RectPeri()
         