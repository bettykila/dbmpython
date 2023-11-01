try:
     
    class Rectangle: 

        def __init__(self,length,width):
            self.length = length
            self.width = width
        
        def RectArea(self):
            print ("Area is: ", (self.length * self.width), " cm2")
    
        def RectPeri(self):
            print ("Perimeter is: ", (2*self.length + 2*self.width), " cm")

    Userlength = int(input("Enter length (cm): "))
    Userwidth = int(input("Enter Width (cm): "))

    RectObj = Rectangle (Userlength, Userwidth)

    #RectObj.RectPeri()
    RectObj.myfunction

except SyntaxError:
    print("Please check for missing colon or possible syntax error")

except AttributeError:
    print("Method not found. Use correct method")