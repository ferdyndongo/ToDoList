#!/usr/bin/env python3
from crud import insert_task, print_today, exit_task, recreate_database,\
    weeks_tasks, all_tasks, missed_tasks, delete_task

recreate_database()

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
    today_task = input()
    if today_task == '1':
        print_today()
    elif today_task == '2':
        weeks_tasks()
    elif today_task == '3':
        all_tasks()
    elif today_task == '4':
        missed_tasks()
    elif today_task == '5':
        insert_task()
    elif today_task == '6':
        delete_task()
    elif today_task == '0':
        today_task = exit_task()
