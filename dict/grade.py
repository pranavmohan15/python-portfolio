marks={"Arun":[80,75,90],"Meera":[60,70,65]}
grades={}
print("______STUDENTS GRADE______")
print("NAME\tTOTAL\tAVERAGE\tGRADE")
print("--------------------------------")
for name,scores in marks.items():
    total=sum(scores)
    avg=total/len(scores)

    if avg>=90:
        grade='A'
    elif avg>80 and avg<90:
        grade='B'
    elif avg>70 and avg<80:
        grade='C'
    elif avg>60 and avg<70:
        grade='D'
    else:
        grade='F'
    grades[name]=grade
    print(f"{name}\t{total}\t{avg:.2f}\t{grade}")