class Demo():
    def __init__(self,name,age):
        self.name1=name #public attribute
        self.age1=age   #public attribute
    def display(self):
        print("Age",self.age1)

obj=Demo("pranav",20)
print("name",obj.name1)
obj.display()


