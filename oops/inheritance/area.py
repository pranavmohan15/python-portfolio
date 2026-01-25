class Shape:
    def area(self):
        print("area displayed")

    
class Rectangle(Shape):
   def cal(self,l,w):
       print(l*w)
       
    
# height=print("enter the height:")
# width=print("enter the width:")
obj=Rectangle()
obj.area()
obj.cal(9,2)

    
    

    