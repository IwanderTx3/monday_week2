import os
os.system('clear')

task_list = []
title = ''
priority = 0
current_task = None

class Task:
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority
    
    def __repr__(self):
        return (f"{self.title} with a priority of {self.priority} ")

def add_task():
    title = input("What is this task? ")
    priority = int(input("On a scale of 1 to 9 with 1 being not important and 9 being URGENT.  How important is this task?  "))
    task_list.append(Task(title,priority))

def list_tasks():
    for i in range(len(task_list)):
        print (task_list[i])

def remove_tasks():
    list_tasks(task_list)
    got_to_go = input("What task do you want to remove? ")
    task_list.remove(got_to_go)

def sort_tasks():
    sort = input("Do you want to sort ascending or decending? (a or d) ")
    if sort == 'a' :
        for check in range(len(task_list)-1,0,-1):
            for i in range(check):
                if task_list[i] > task_list[i+1]:
                    temp = task_list[i]
                    task_list[i] = task_list[i+1]
                    task_list[i+1] = temp
    elif sort == 'd' :
        for check in range(len(task_list)-1,0,-1):
            for i in range(check):
                if task_list[i] < task_list[i+1]:
                    temp = task_list[i]
                    task_list[i] = task_list[i+1]
                    task_list[i+1] = temp
    else:
        print("Please select either a or d")

def pause():
    input("Press Enter to continue")
    action_list()

def action_list():
    os.system('clear')
    print(' 1) List Tasks')
    print(' 2) Add Task')
    print(' 3) Remove Task')
    print(' 4) Sort Tasks')
    print(' Q) Exit ')
    action = input()

    if action == '1':
        list_tasks()
        pause()
    elif action == '2':
        add_task()
        pause()
    elif action == '3':
        remove_tasks()
        pause()
    elif action == '4':
        sort_tasks()
        pause()
    elif action == 'q':
        exit
    else:
        print("invalid selection")
        input()
        action_list()

#task_list.append(Task('scream',9))
#print(task_list[-1])
pause()
action_list()