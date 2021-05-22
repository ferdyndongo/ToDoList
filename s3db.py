#!/usr/bin/env python3
from datetime import datetime, timedelta


# create table
def create_table_task(con):
    cur = con.cursor()
    cur.execute('create table if not exists task(id integer primary key autoincrement, task text, deadline datetime);')
    con.commit()
    cur.close()


# drop table
def drop_table_task(con):
    cur = con.cursor()
    cur.execute('drop table if exists task;')
    con.commit()
    cur.close()


def recreate_table_task(con):
    drop_table_task(con)
    create_table_task(con)


def print_task(today, tasks, *date):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if not date:
        if len(tasks) == 0:
            print(f"\n{weekdays[today.date().weekday()]} {today.date().day} {today.date().strftime('%b')}:")
            print("Nothing to do!")
        else:
            print(f"""\n{weekdays[today.date().weekday()]} {today.date().day} {today.date().strftime('%b')}:""")
            for index, task in enumerate(tasks):
                print(index + 1, task[1], sep='. ')
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task[1]}. {datetime.strptime(task[2], '%Y-%m-%d').day} {datetime.strptime(task[2], '%Y-%m-%d').strftime('%b')}")


def read_task(con, **delta):
    today = datetime.today()
    if not delta:
        cur = con.cursor()
        tasks = cur.execute('select * from task order by deadline;').fetchall()
        if len(tasks) != 0:
            print_task(today, tasks, 'all')
        cur.close()
        return tasks
    else:
        if delta['delta'] >= 0:
            for day in range(delta['delta'] + 1):
                cur = con.cursor()
                cur_date = today + timedelta(days=day)
                tasks = cur.execute('select * from task where deadline = ?;', (cur_date.date().strftime('%Y-%m-%d'),)).fetchall()
                print_task(cur_date, tasks)
                cur.close()
            return tasks
        else:
            cur = con.cursor()
            tasks = cur.execute('select * from task where deadline < ? order by deadline;', (today.date(),)).fetchall()
            print("\nMissed tasks:")
            if len(tasks) == 0:
                print("Nothing is missed!")
                cur.close()
            else:
                print_task(today, tasks, 'missed')
                cur.close()
            return tasks


def insert_task(con):
    task = input("""
Enter task
""")
    deadline = datetime.strptime(input("""Enter deadline
"""), '%Y-%m-%d')
    cur = con.cursor()
    cur.execute('insert into task (task, deadline) values(?, ?)', (task, deadline.date()))
    con.commit()
    cur.close()
    print("""The task has been added!""")


def delete_task(con):
    tasks = read_task(con)
    if len(tasks) == 0:
        print("\nNothing to delete")
    else:
        print("Choose the number of the task you want to delete:")
        d = int(input())
        cur = con.cursor()
        cur.execute('delete from task where task = ? and deadline = ?;', (tasks[d-1][1], tasks[d-1][2]))
        con.commit()
        cur.close()
        print("The task has been deleted!")


def exit_task(con):
    con.close()
    print("\nBye!")
    return 0
