File: attendance.txt
John,85
Alice,72
David,60
Emma,90
Sophia,68



f = open("attendance.txt", "r")
for line in f:
    name, percent = line.strip().split(",")
    if float(percent) < 75:
        print(name, "has low attendance (", percent, "% )")
f.close()
