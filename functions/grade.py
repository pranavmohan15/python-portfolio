def grad_calculator(mark):
    if mark>=90:
        return "A"
    elif mark<90 and mark>=75:
        return "B"
    elif mark<75 and mark>=50:
        return "C"
    elif mark<50:
        return "F"
mark=int(input("enter the mark of the student:"))
print(grad_calculator(mark))
