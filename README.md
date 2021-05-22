# To-Do List
## About
To-Do list can improve your work and personal life. You can use it to reduce the stress in your life and get more done
in less time. It also helps you become more reliable for other people and save time for the best things in life.
## Description
This project is about implementing a To-Do list that will help you manage your tasks and organize your life. It's very
upsetting when the data about your to-do tasks disappear after the program is completed. To avoid this problem, we will
create a database where we can store all the necessary information about tasks. We will use **SQLite** to create the 
database and **SQLAlchemy** to manage the database from python. SQLAlchemy is the python SQL toolkit and Object Relational
Mapper (ORM) that gives developers the full power of flexibility of SQL.
## Objectives
1. Create a database file named `todo.db`
3. Create a table named `task` in this database with the following columns:
    * Integer column named `id`. It should be `primary key`
    * String column named `task`
    * Date column named `deadline`. It should have the date when the task was created by default. 
4. Implement a menu that will make your program more convenient:
   ![menu.png](menu.png)
    * **Today's tasks**: prints all tasks for today.
    * **Add task**: Asks for task description and its deadline, and saves it in the database.
    * **Week's tasks**: prints all tasks for 7 days from today.
    * **All tasks**: prints all tasks sorted by deadline.
    * **Missed tasks**: prints all tasks whose deadline was missed, that is, tasks whose deadline date is earlier than
      today's date. It should print the tasks ordered by the deadline date.
    * **Delete tasks**: deletes the chosen task. Print `Nothing to delete` if the tasks list is empty. It should print
   all the tasks sorted by the deadline date and ask to enter the number of the task to delete.
5. Implement the ability to see missed tasks and delete them.
