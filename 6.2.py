File: salary.txt
101,Arun,50000
102,Bhavya,60000
103,Chitra,55000
104,Deepak,45000



emp_id = input("Enter Employee ID to update: ")
new_salary = input("Enter new salary: ")

lines = []
f = open("salary.txt", "r")
for line in f:
    eid, name, sal = line.strip().split(",")
    if eid == emp_id:
        line = eid + "," + name + "," + new_salary + "\n"
    lines.append(line)
f.close()

f = open("salary.txt", "w")
f.writelines(lines)
f.close()
print("Salary updated successfully.")
