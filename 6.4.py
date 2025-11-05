File: system.log

INFO: System started successfully
WARNING: Low memory detected
ERROR: Disk not found
INFO: User logged in
ERROR: Connection failed



count = 0
f = open("system.log", "r")
for line in f:
    if "ERROR" in line:
        count += 1
f.close()
print("Total ERROR messages:", count)
