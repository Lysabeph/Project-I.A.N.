logs_array = []

with open("logs.txt", "r") as log_file:
    for line in log_file:
        logs_array.append(log_file.readline().split(" "))

programs = {}
x = 1

for log in logs_array:
    if log[1] not in programs:
        programs[log[1]] = x
        x+=1
