rect_list=[]
with open('rectangles.txt') as line:
    while True:
        inst=line.readline().rstrip()
        if not inst:
            break
        else:
            rect_list.append(inst)

# print(rect_list)

class Rectangle():
    """blah blah blah"""
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def get_area(self):
        return self.length*self.width

nbr=1
for item in rect_list:
    split=item.split(',')
    length,width=int(split[0]),int(split[1])
    area=Rectangle(length,width).get_area()
    print(f"Rectangle #{nbr} area is {area}")
    nbr+=1

line.close()