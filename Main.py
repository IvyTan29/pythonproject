from os import system, name 
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

enlistment = Enlistment()
use = True
while use:
    print (".--. .    .-. .   .  .---.     .          .                   .  ")
    print ("|   :|   (   )|   |  |         |   o     _|_                 _|_ ")
    print ("|   ||    `-. |   |  |--- .--. |   .  .--.|  .--.--. .-. .--. |  ")
    print ("|   ;|   (   ):   ;  |    |  | |   |  `--.|  |  |  |(.-' |  | |  ")
    print ("'--' '---'`-'  `-'   '---''  `-`--' `-`--'`-''  '  `-`--''  `-`-'")
    print ("\n\t\t\tWelcome~~")
    ans = input ("\nAre you new to this enlistment system? (y/n) ")

    while not(ans.lower() == 'y' or ans.lower() == 'n'):
        print ("Invalid Input! Try again.")
        ans = input ("Are you new to this enlistment system? (y/n) ")
        
    idnumber = input ("Enter idnumber: ")
    password = input ("Enter password: ")

    if (ans.lower() == 'y'):
        usertype = input ("Are you an admin or student? (a/s) ")

        while not(usertype.lower() == 'a' or usertype.lower() == 's'):
            print ("Invalid Input! Try again.")
            usertype = input ("Are you an admin or student? (a/s) ")

        if (usertype.lower() == 'a'):
            user = Admin (idnumber, password)
            enlistment.addUser (user)
        else:
            user = Student (idnumber, password)
            enlistment.addUser (user)

    elif (ans.lower() == 'n'):
        isFound = False
        index = ""
        i = 0
        # for i in range(len(users)):
        #     if (users[i].getIDNumber() == idnumber):
        #         isFound = True
        #         index = i

    use = False
