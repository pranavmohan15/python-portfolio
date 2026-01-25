#represented by ('_')
#members should not access out side the classs but access the subclass
class Students:
    def __init__(self,name,roll,branch):
        self._name=name
        self._roll=roll
        self._branch=branch
    def _displayrollandbranch(self):
        print("Roll_No:",self._roll,"Branch_Name:",self._branch)

class School(Students):
    def display(self):
        print("name",self._name)

obj=Students("pranav",1,"py")
obj._displayrollandbranch()
obj._name #it is not printing bcz it is outside the class and the subclass so it cant print


        
    
