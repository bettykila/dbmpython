class Triangle ():
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def TriArea(self):
        print("Area is: ", (self.base * self.height) /2)
    
    def TriPeri(self):
        print("Perimeter is: ", (self.base*3))

Userbase = int(input("Enter base (cm)"))
Userheight = int(input("Enter height (cm)"))

#object instantiation . Attach to class only with parameters
TriObj = Triangle (Userbase, Userheight)

#use the object created. Call function here.
TriObj.TriArea()
TriObj.TriPeri()
    
