def grade(mark):
    if mark>=90:
        return "Excellent!!!!"
    elif mark>=80 and mark<90:
        return "Good!!!!!"
    elif mark>=70 and mark<80:
        return "Average!!!!"
    elif mark<70:
        return "Poor!!!!"
mark=int(input("enter the mark:"))
print(grade(mark))