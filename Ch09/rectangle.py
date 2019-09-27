class Rectangle():
    """Holds width and lengthe and calcualtes area"""
    #class variables
    area_formula="area = length * width"
    
    #instance variable
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def get_area(self):
        return self.length*self.width

rect1=Rectangle(12,10)
rect2=Rectangle(5,4)

print(rect1.get_area())

print(rect1.area_formula)
print(rect2.area_formula)
rect1.area_formula="area = length*width"
print(rect1.area_formula)
print(rect2.area_formula)

Rectangle.area_formula="area = length*width"
print(rect1.area_formula)
print(rect2.area_formula)
