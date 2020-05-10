## TODO: Error Handling 
## TODO: Databases 

import pdb
import os

def main():
    todo_list = ToDoList()

    while(True):
        clear_screen()
        todo_list.show_task()
        print("\n")
        print(asterisk_message(60, 8,
            '''
            Hello! Welcome to my TODO application
              What would you like to do?
              [1] To add a new todo item 
              [2] To complete a todo item 
              [3] To delete a todo item'''))
        
        print("\n")
        choose = int(input())
        print("\n")
        
        if choose ==1: 
            print("> Give me the task:")
            taskname = input()
            print("\n")
            print("> Give me the priority:\n")
            priority = int(input())
            print("\n")
            clear_screen()
            tmp_task1 = Task(taskname, priority, complete="N")
            todo_list.new_task_new(priority, tmp_task1)

        elif choose==2:
            print(">Please input the index of the task")
            index=int(input())
            clear_screen()
            complete_task = todo_list.tasks[index]
            complete_task.complete = "Y"

        else:
            print("> Please input the index of the task you want to delete")
            delete=int(input())
            clear_screen()
            lists= todo_list.tasks
            del lists[delete]

# From: https://stackoverflow.com/questions/52650641/how-make-a-box-or-rectangle-from-asterisks-using-for-loops-in-python
def asterisk_box(width, height):
    'Create a box of asterisks and return it as a string'
    assert height >= 2  # Make sure we actually have a box
    assert width >= 2   # Make sure we actually have a box
    box = '*' * width + '\n'
    for _ in range(height - 2):
        box += '*' + ' ' * (width - 2) + '*\n'
    box += '*' * width
    return box

def asterisk_message(width, height, message):
    'Put a message within the asterisk box'
    assert height >= 3                # Make sure there is room for a message
    #assert len(message) <= width - 2  # Make sure the box is wide enough
    box = asterisk_box(width, height)
    box = box.splitlines()
    row = height // 2
    box[row] = '*' + message.center(width - 2) + '*'
    return '\n'.join(box)

def clear_screen():
    os.system('clear')

class Task:
    def __init__(self,task_name,priority,complete=""):
        self.task_name = task_name
        self.priority = priority
        self.complete = "N"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def new_task_new(self,priority_,task):
        self.tasks.insert(priority_, task)

    def show_task(self):
        tasks = self.tasks
        num_tasks=len(self.tasks)
        print('You have {} task to do today'.format(num_tasks))
        for task in tasks:
            print('[{}] {}'.format(task.complete,task.task_name))


if __name__ == '__main__': main()



