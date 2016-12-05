#!/usr/bin/python3

import sqlite3
import time

HOUR = 3600
DAY = 86400
WEEK = 604800

UPDATE_INTERVAL = HOUR # Default is every hour.

def get_time_range(epoch):
    current_epoch = epoch
    lower_epoch = current_epoch - current_epoch % UPDATE_INTERVAL
    upper_epoch = lower_epoch + UPDATE_INTERVAL
    return lower_epoch, upper_epoch

def condition_checker(program, logs, open_programs, count = 0):
    if count < len(open_programs) - 1:
        if open_programs[count] in logs:
            condition_checker(program, logs, open_programs, count += 1)
        else:
            return False
    else:
        return True

conn = sqlite3.connect('test.db')
c = conn.cursor()

programs = []

for record in c.execute("""
                            SELECT *
                            FROM Programs;
                        """):
     programs.append(record[0])

print(programs)

#with open("open_programs", "r") as file:
#    open_programs = file.readlines()
open_programs = []

current_epoch = 1478968907 # int(time.time())
lower_epoch, upper_epoch = get_time_range(current_epoch)

c.execute("""
            SELECT *
            FROM ProgramLogs
            ORDER BY DateTime ASC Limit 1;
        """)
first_epoch = c.fetchone()[-2]

logs = []

while upper_epoch > first_epoch:
    print(lower_epoch, upper_epoch)
    range_log = []

    # Put open_program check thingy here!!!
        
    for log in c.execute("""
                            SELECT *
                            FROM ProgramLogs
                            AND ProgramLogs.OpenClose='Open'
                            AND ProgramLogs.DateTime>='{0}'
                            AND ProgramLogs.DateTime<'{1}';
                        """.format(str(lower_epoch), str(upper_epoch))):
        range_logs.append(log[0])
        logs.append(log)

    for prog in open_programs:
        if prog in range_logs:
            continue
        else:
            prog = False
            break

    lower_epoch-=DAY
    upper_epoch-=DAY
    
for program in programs:

    if "\'" + program + "\'" in open_programs:
        continue

    c.execute("""
                SELECT *
                FROM ProgramLogs
                WHERE ProgramLogs.ProgramName='{0}'
                ORDER BY DateTime ASC Limit 1;
            """.format(program))
    
    earliest_epoch = c.fetchone()[-2]
    print(earliest_epoch)

    program_logs = list(logs)

    # Using logs as the length of the array will be static throughout the loop.
    for record in logs:
        if record[2] < earliest_epoch:
            program_logs.remove(record)
    
    times_run = []
    program_log_counter = 0
        
    for record in logs:
        if record[0] == program:
            program_log_counter += 1

    times_run.append(program_log_counter)

# ~~~

    lower_epoch, upper_epoch = get_time_range(current_epoch)

    # Checks if the currently open programs have been open togother in the past.
    # This could be done exactly (so no extra programs were open with the current
    # set-up) but this may not be useful.
    while upper_epoch > first_epoch:
        for prog in open_programs:
            if prog in logs 

    condition_checker(program, logs, open_programs)

# ~~~

    summ = 0
    for num in times_run:
        if num > 0:
            summ+=1
    prob = summ/len(times_run)
    pers = sum(array)//len(times_run)

    programs[programs.index(program)] = [program, times_run, prob, pers]
    

for program in programs:
    print(program)
