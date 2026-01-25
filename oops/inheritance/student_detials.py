class Person:
    def __init__(self,name,age):
        self.n1=name
        self.a1=age
class Student(Person):
    def __init__(self, name, age,course):
        super().__init__(name, age)
        self.c1=course
    def show(self):
        print('--student Details')
        print('name:',self.n1)
        print('age:',self.a1)
        print('course:',self.c1)
name=input("enter the name:")
age=int(input('enter your age:'))
course=input('enter your course:')

obj=Student(name,age,course)
obj.show()        