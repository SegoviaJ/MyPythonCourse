import math

class Circle():
    """Uses radius to calculate area"""
    def __init__(self,rad):
        self.rad=rad
    def circle_area(self):
        return math.pi*self.rad**2

circle1=Circle(5)
print(circle1.circle_area())