#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

#    def __repr__(self):
#        return str(self.id) + '. ' + self.task


engine = create_engine('sqlite:///todo.db?check_same_thread=False')


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)


def print_today(date=datetime.today().date()):
    session = Session()
    tasks = session.query(Task).filter(Task.deadline == date).all()
    if len(tasks) == 0:
        print(f"""
Today {date.day} {date.strftime('%b')}:
Nothing to do!""")
    else:
        print(f"\nToday {date.day} {date.strftime('%b')}:")
        for index, task in enumerate(tasks):
            print(index + 1, task.task, sep='. ')


def print_task(today, tasks):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if len(tasks) == 0:
        print(f"\n{weekdays[today.date().weekday()]} {today.date().day} {today.date().strftime('%b')}:")
        print("Nothing to do!")
    else:
        print(f"""\n{weekdays[today.date().weekday()]} {today.date().day} {today.date().strftime('%b')}:""")
        for index, task in enumerate(tasks):
            print(index + 1, task.task, sep='. ')


def list_task(tasks):
    for index, task in enumerate(tasks):
        deadline = task.deadline
        print(f"{index + 1}. {task.task}. {deadline.day} {deadline.strftime('%b')} ")


def weeks_tasks():
    session = Session()
    for i in range(7):
        day = datetime.today() + timedelta(days=i)
        tasks = session.query(Task).filter(Task.deadline == day.date()).all()
        print_task(day, tasks)


def all_tasks():
    session = Session()
    tasks = session.query(Task).order_by(Task.deadline).all()
    print("\nAll tasks:")
    list_task(tasks)


def insert_task():
    new_task = input("""
Enter task
""")
    new_deadline = datetime.strptime(input("""Enter deadline    
"""), '%Y-%m-%d')
    session = Session()
    add_task = Task(task=new_task, deadline=new_deadline.date())
    session.add(add_task)
    session.commit()
    session.close()
    print("The task has been added!")


def missed_tasks():
    session = Session()
    tasks = session.query(Task).filter(Task.deadline < datetime.today().date()).order_by(Task.deadline).all()
    print("\nMissed tasks:")
    if len(tasks) != 0:
        list_task(tasks)
    else:
        print("Nothing missed")


def delete_task():
    session = Session()
    tasks = session.query(Task).order_by(Task.deadline).all()
    if len(tasks) == 0:
        print("\nNothing to delete")
    else:
        print("\nChoose the number of the task you want to delete:")
        list_task(tasks)
        d = int(input())
        session.query(Task).filter(Task.task == tasks[d-1].task and Task.deadline == tasks[d-1].deadline).delete()
        session.commit()
        session.close()
        print("The task has been deleted!")


def exit_task():
    print("\nBye!")
    return 0
