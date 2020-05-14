import pdb
#pdb.set_trace()
import os
import pickle 

file_name = 'programming.pkl'

def main():
    todo_list = ToDoList()

    try:
        with open(file_name, 'rb+') as output:
            new_lst1 = pickle.load(output)
    except EOFError:
        new_lst1 = []

    while(True):
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

        acceptable_commands=[1,2,3]

        if choose not in acceptable_commands:
            print("Please type in 1, 2 or 3")
            print("Press any key to continue")
            choice = input()
            if choice != None:
                clear_screen()
                continue

        if choose ==1: 
            print("> Give me the task:")
            taskname = str(input())
            print("\n")
            print("> Give me the priority:\n")
            priority = int(input())
            print("\n")
            clear_screen()
            tmp_task1 = Task(taskname, priority, complete="N")
            todo_list.new_task_new(priority, tmp_task1)
            new_new_lst = new_lst1 + todo_list.tasks

            with open(file_name, 'wb+') as output:
                pickle.dump(new_new_lst, output)
            

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
        
        clear_screen()

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
        try:
            with open(file_name, 'rb') as output:
                new_list = pickle.load(output)
        except EOFError:
            new_list = []

        num_tasks=len(new_list)
        print('You have {} task to do today'.format(num_tasks))
        for task in new_list:
            print('[{}] {}'.format(task.complete,task.task_name))


if __name__ == '__main__': 
    main()



