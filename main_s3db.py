#!/usr/bin/env python3


import sqlite3
from s3db import read_task, insert_task, exit_task, recreate_table_task, delete_task, print_task

# create db and/or connect to it with sqlite3
con = sqlite3.connect('todo.s3db')

# create or recreate table if it exists
recreate_table_task(con)


today_task = ''
while today_task != 0:
    print("""
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit""")
    today_task = int(input())
    if today_task == 1:
        read_task(con, delta=0)
    elif today_task == 2:
        read_task(con, delta=7)
    elif today_task == 3:
        print("\nAll:")
        read_task(con)
    elif today_task == 4:
        read_task(con, delta=-1)
    elif today_task == 5:
        insert_task(con)
    elif today_task == 6:
        delete_task(con)
    elif today_task == 0:
        today_task = exit_task(con)
