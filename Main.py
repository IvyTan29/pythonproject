from os import system, name 
from time import sleep
from Enlistment import Enlistment
from Admin import Admin
from Student import Student
from User import User
from Class import Class

def clear(): 
    if name == 'nt': # windows 
        _ = system('cls') 
    elif name == 'posix': # mac and linux
        _ = system('clear') 

def pause():
    if name == 'nt': # windows 
        print ("Press any key to continue...")
        _ = system("pause")
    elif name == 'posix': # mac and linux
        _ = system('read -sn 1 -p "Press any key to continue..."')

enlistment = Enlistment()
use = True
while use:
    print (".--. .    .-. .   .  .---.     .          .                   .  ")
    print ("|   :|   (   )|   |  |         |   o     _|_                 _|_ ")
    print ("|   ||    `-. |   |  |--- .--. |   .  .--.|  .--.--. .-. .--. |  ")
    print ("|   ;|   (   ):   ;  |    |  | |   |  `--.|  |  |  |(.-' |  | |  ")
    print ("'--' '---'`-'  `-'   '---''  `-`--' `-`--'`-''  '  `-`--''  `-`-'")
    print ("\n\t\t\tWelcome~~")

    print ("\t\t", end = '')
    pause() 
    clear()

    enlistment.LogInPage()

    menu = True
    while menu:   
        clear()

        print ("\t\t\tMenu")
        print ("\t\t[1] View All Classes")

        
        if (isinstance(enlistment.getCurrentUser(),Admin)):
            print ("\t\t[2] Add Class")
            print ("\t\t[3] Remove Class")
            admin_dict = {2 : enlistment.getCurrentUser().addClass, 3 : enlistment.getCurrentUser().removeClass, 1: enlistment.viewClasses, 4: enlistment.LogInPage}
        elif (isinstance(enlistment.getCurrentUser(),Student)):
            print ("\t\t[2] Take Class")
            print ("\t\t[3] Drop Class")
            student_dict = {2 : enlistment.getCurrentUser().takeClass, 3 : enlistment.getCurrentUser().dropClass,1: enlistment.viewClasses, 4: enlistment.LogInPage}
            
        print ("\t\t[4] Log-Out")
        print ("\t\t[5] Exit")

        ans = input("Choice of action: ")

        while not(ans >= '1' and ans <= '5'):
            print ("Invalid Input! Try again.")
            ans = input("Choice of action: ")

        clear()

        if (ans == '5'):
            menu = False

        elif (isinstance(enlistment.getCurrentUser(),Student) and (ans == '2' or ans == '3')):
            enlistment.viewClasses()
            choice =print ("\nChoose classes: ")

            while not(ans >= '1' and ans <= str(len(enlistment.getClasses()))):
                print ("Invalid Input! Try again.")
                choice = print ("\nChoose classes: ")

            student_dict[int(ans)](enlistment.getClasses()[int(choice-1)])
            
        elif (isinstance(enlistment.getCurrentUser(),Admin)):
            admin_dict[int(ans)]()

        elif (isinstance(enlistment.getCurrentUser(),Student)):
            student_dict[int(ans)]()

        pause()

    clear()

    ans = input ("Are you going to exit or restart the enlistment system? (e/r) ")

    while not(ans.lower() == 'e' or ans.lower() == 'r'):
            print ("Invalid Input! Try again.")
            ans = input ("Are you going to exit or restart the enlistment system? (e/r) ")

    clear()

    for i in range(3,0,-1):
        if (ans == 'e'):
            print ("\t\t\tExiting... ",i, end = '')
            use = False
        elif (ans == 'r'):
            print ("\t\t\tRestarting...",i, end = '')
            use = True
        sleep(1)
        clear()
