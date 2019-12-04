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

    ans = input ("\nAre you new to this enlistment system? (y/n) ")

    while not(ans.lower() == 'y' or ans.lower() == 'n'):
        print ("Invalid Input! Try again.")
        ans = input ("Are you new to this enlistment system? (y/n) ")

    idnumber = input ("Enter ID Number: ")
    password = input ("Enter Password: ")

    isFound = False
    index = -1
    i = 0
    for i in range(len(enlistment.getUsers())):
        if (enlistment.getUsers()[i].getIDNumber() == idnumber):
            isFound = True
            index = i

    if (isFound):
        print ("\nThe system detected that your ID number have already been registered.")
        ans = 'g' #any char would do as long as it is not y or n

    if (not isFound and ans == 'n'):
        print ("\nThe system detected that your ID number have not been registered.")
        ans = 'y'
        print ("Proceed to the initial registration part.")

    if (ans.lower() == 'y'):
        usertype = input ("\nAre you an admin or student? (a/s) ")

        while not(usertype.lower() == 'a' or usertype.lower() == 's'):
            print ("Invalid Input! Try again.")
            usertype = input ("Are you an admin or student? (a/s) ")

        if (usertype.lower() == 'a'):
            user = Admin (idnumber, password)
            index = len(enlistment.getUsers())
            enlistment.addUser (user)
        else:
            user = Student (idnumber, password)
            index = len(enlistment.getUsers())
            enlistment.addUser (user)

    elif (ans.lower() == 'n'):
        while not enlistment.logIn(idnumber,password, index):
            print ("\nPassword and ID Number does not match")
            password = input ("Retype Password: ")
        
    clear()










    #insert here log out 


    ans = input ("Are you going to exit the enlistment system? (y/n) ")
    clear()

    for i in range(3,0,-1):
        if (ans == 'y'):
            print ("\t\t\tExiting... ",i, end = '')
            use = False
        elif (ans == 'n'):
            print ("\t\t\tRestarting...",i, end = '')
            use = True
        sleep(1)
        clear()
