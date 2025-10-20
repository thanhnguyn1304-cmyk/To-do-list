filename = "C:\\Users\\Yoga\\Desktop\\todo.txt"
with open(filename, "r") as file:
    tasks = [line.strip()+'\n' for line in file.readlines()]


def view(tasks):
    print("Today's list:")
    for i in range(len(tasks)):
        print(f'{i+1}. {tasks[i].rstrip('\n')}')


def add():
    task = str(input('Enter your task for today: \n'))
    task = task.strip().lower().capitalize()
    tasks.append(task + '\n')
    
    print("\n")
    view(tasks)
    
def remove():
    view(tasks)
    task_number = int(input('Which task do you want to remove ?: \n'))
    if task_number <= len(tasks):
        tasks.pop(task_number-1)
    else:
        print('Invalid Option\n')
    
    print("\n")
    view(tasks)

def save_task():
    with open(filename, 'w') as file:
        file.writelines(tasks)


while True:
    print('What you want to do today?\n',
      '1. Add tasks\n',
      '2. View tasks\n',
      "3. Remove tasks if you're done \n",
      '4. Exit\n'
        )
    
    choice = int(input('Enter your choice: '))
    if choice == 1:
        add()
    elif choice == 2:
        view(tasks)
    elif choice == 3:
        remove()
    else:
        save_task()
        print('Goodbye!')
        break
    







# tasks now contains all the lines from tasks.txt
