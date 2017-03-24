# A program to manage tasks using List and its functions

# Initialising the globals
tasks=['Go to computer class','Watch TV serial']
ch=1

# Function to add a new task at the end
def addTsk():
    while True:
        tsk=raw_input("Enter new task(leave blank to exit): ")
        if tsk=="":
            break
        else:
            tasks.append(tsk)

# Function to add a new task at a given position
def insTsk():
    while True:
        tsk=raw_input("Enter new task(leave blank to exit): ")
        if tsk=="":
            break
        else:
            pos=input("Enter position number: ")
            tasks.insert(pos,tsk)

# Function to show all tasks in alphabatical order
def showInOrder():
    temp=[]
    for tsk in tasks:
        temp.append(tsk)
    temp.sort()
    print
    for tsk in temp:
        print tsk,", ",
    print "\n\n"

# Function to show all tasks in actual order
def showTsk():
    print
    for tsk in tasks:
        print tsk,", ",
    print "\n\n"

# Function to remove the last task in the list
def removLsTsk():
    if len(tasks)>0:
        tasks.pop()

# Function to remove any given task from the list
def removAnyTsk():
    if len(tasks)>0:
        tsk=raw_input("Enter task to be removed: ")
        tasks.remove(tsk)

# Function to give priority to any task by moving task to first position
def prioriTsk():
    if len(tasks)>0:
        tsk=raw_input("Enter task to be removed: ")
        tasks.remove(tsk)
        tasks.insert(0,tsk)

# Function to show and get choice of tasks
def menu():
    global ch
    print
    print "\t\t\t1. Add new task"
    print "\t\t\t2. Insert new task where you want"
    print "\t\t\t3. Show all tasks"
    print "\t\t\t4. Remove last task"
    print "\t\t\t5. Remove any task"
    print "\t\t\t6. Give priority to a task"
    print "\t\t\t7. Show in alphabatical order"
    print "\t\t\t8. Exit program"
    ch=int(input("\t\t\tEnter choice no.: "))

# Executing whole program with user's choice
while ch<8:
    #print ch
    #dummy=input("Press enter to continue . . . .")
    menu()
    if ch==1:
        addTsk()
    elif ch==2:
        insTsk()
    elif ch==3:
        showTsk()
    elif ch==4:
        removLsTsk()
    elif ch==5:
        removAnyTsk()
    elif ch==6:
        prioriTsk()
    elif ch==7:
        showInOrder()

