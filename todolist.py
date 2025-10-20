filename = "C:\\Users\\Yoga\\Desktop\\todo.txt"
with open(filename, "r") as file:
    tasks = [line.strip()+'\n' for line in file.readlines()]

def save_task():
    with open(filename, 'w') as file:
        file.writelines(tasks)

def view(tasks):
    print('\n')
    print("Today's list:")
    if not tasks :
        print('No tasks for today!') #Handle empty list
    else:
        for i in range(len(tasks)):
            print(f'{i+1}. {tasks[i].rstrip('\n')}')
    
def add():
    task = str(input('Enter your task for today: \n'))
    tasks.append(task.strip().lower().capitalize() + '\n')
    save_task() #Save immediately
    print("\n")
    view(tasks)
    
def remove():
    view(tasks)
    try: #Handle false input
        task_number = int(input('Which task do you want to remove ?: \n'))
        if task_number <= len(tasks):
            tasks.pop(task_number-1)
        else:
            print('Invalid Option\n')
        save_task()
        print("\n")
    except ValueError:
        print('Invalid input! Please enter a number: ')
    view(tasks)

def save_task():
    with open(filename, 'w') as file:
        file.writelines(tasks)


while True:
    print('What you want to do today?\n',
      '1. Add tasks\n',
      '2. View tasks\n',
      "3. Remove tasks if you're done \n",
      '4. Exit'
        )
    
    try: # If the number is not an intenger
        choice = int(input('Enter your choice: '))
    except ValueError:
        print('Invalid input! Please enter a number: ')
        pass
    if choice == 1:
        add()
    elif choice == 2:
        view(tasks)
    elif choice == 3:
        remove()
    elif choice ==4:
        save_task()
        print('Goodbye!')
        break
    else: # If the number is not between 1 and 4
        print('Invalid choice, please choose again!')
    






