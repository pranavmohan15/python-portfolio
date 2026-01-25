employees={
    101:{"name":"amit","dept":"HR","salary":40000},
    102:{"name":"neha","dept":"IT","salary":60000},

}
while True:
    print("1.add employee")
    print("2.update the salary of an existing employee")
    print("3.remove an employee by id")
    print("4.display all employee details")
    print("5.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        emp_id=int(input("enter the employeeid:"))
        name=input("enter the name:")
        dept=input("enter the dept:")
        salary=int(input("enter the salary:"))
        employees[emp_id]={"name":name,"dept":dept,"salary":salary}
        print("details added")
        print(employees)
        
    elif choice==2:
        new_empid=int(input("enter your employee id:"))
        if new_empid in employees:
            new_salary=int(input("enter the salary:"))
            employees[new_empid].update({"salary":new_salary})
            print("salary updated")
        else:
            print("there is no emploeyee id in employees")

    elif choice==3:
        emp_id=int(input("enter the employeed id want to delete:"))
        if emp_id in employees:
            employees.pop(emp_id)
            print("removed successfully")
        else:
            print("employee id is not found")

        
    elif choice==4:
        print("\nEmployee Details")
        print("ID\tName\tDept\tSalary")
        total=0
        for id,info in employees.items():
            print(f"{id}\t{info['name']}\t{info['dept']}\t{info['salary']}")
            total+=info['salary']
        print(f"\ntotal salary:{total}")
        print(f"average salary:{total/len(employees)}")        
    elif choice==5:
        break
    else:
        print("enter a valid option")


























# employees.update({103:{"name":"pranav","dept":"IT","salary":70000},})
# employees[104]={"name":"kichu","dept":"IT","salary":90000}

# employees[101].update({"salary":100000})

# employees.pop(102)
# print(employees)

# print("EmpID\tName\tDept\tSalary")
# print("----------------------------------")
# total_salary=0
# for key,value in employees.items():
#     print(f"{key}\t{value['name']}\t{value['dept']}\t{value['salary']}")
#     total_salary+=value["salary"]

# average_salary=total_salary/len(employees)

# print(f"Total Salary = {total_salary}")
# print(f"Average Salary = {average_salary}")