#Keenan Githu
#Lab 6
#December 2, 2024
#SE116.02

#PROGRAM PROMPT: 
"""
Construct a program that will analyze potential voters.
"""

#VARIABLE DICTIONARY:
"""
not_eligible = counts the amount of people not eligible to vote 
not_registered = counts the amount of people not registered to vote
not_voted = counts the amount of people who didn't vote
voted = counts the amount of people who voted
processed = counts the amount of people processed
main = variable used to loop through main code block
loop = used for nested loop inside main code block

"""

#NOTES: none

#some fun clear screen stuff
from os import system, name
def clear():
    if name == 'nt': #for windows
        _ = system('cls')
    else: #for mac and linux
        _ = system('clear')

#i didn't want to copy and paste the message each time
def invalid_message():
    print("\n\t***Invalid Input***\n")

#function to add one to every variable that requires 1 to be added to it
def add_one(plus):
    plus = plus + 1
    return plus

#main code loop variable
main = True

#all the other variables, displayed and stored
not_eligible = 0
not_registered = 0
not_voted = 0
voted = 0
processed = 0

#clear the screen
clear()

#loop main code
while main == True:
    #make loop true so 2nd while loop can run (made false each instance)
    loop = True
    while loop == True:
        #ask for id number
        id_number = input("Enter the ID number: ")
        #try to turn the id_number into an integer, if not, display error message and restart 2nd loop
        try:
            id_number = int(id_number)
        except:
            invalid_message()
            continue
        
        #ask for age
        age = input("Enter the age of the voter: ")
        #try to turn the age into an integer, if not, display error message and restart 2nd loop
        try:
            age = int(age)
        except:
            invalid_message()
            continue
        #if the age entered is less than 18, add one to not_eligible, end 2nd loop
        if age < 18:
            not_eligible = add_one(not_eligible)
            loop = False
            continue
        
        #asks if they're registered to vote, lowers the input
        registered_to_vote = input("Are you registered to vote? [y/n]: ").lower()
        #loop if invalid input
        while registered_to_vote != 'y' and registered_to_vote != 'n':
            invalid_message()
            registered_to_vote = input("Are you registered to vote? [y/n]: ").lower()
        #if the user isn't registered to vote, add one to not_registered, end 2nd loop
        if registered_to_vote == 'n':
            not_registered = add_one(not_registered)
            loop = False
            continue
        
        #ask if they voted
        actually_voted = input("Did you vote? [y/n]: ").lower()
        #loop if invalid input
        while actually_voted != 'y' and actually_voted != 'n':
            invalid_message()
            actually_voted = input("Did you vote? [y/n]: ").lower()
        #if they did vote, add one to voted variable
        if actually_voted == 'y':
            voted = add_one(voted)
        #if they didn't, add one to not_voted
        else:
            not_voted = add_one(not_voted)
        #end 2nd loop
        loop = False

    #runs only after at least one instance of the 2nd loop
    #adds one to processed, as long as a valid age and id_number was inputted
    processed = add_one(processed)

    print("\n")
    #asks the user if they want to enter more data, lowers the input
    repeat = input("Would you like to enter more data? [y/n]: ").lower()
    #loops if invalid input
    while repeat != 'y' and repeat != 'n':
        invalid_message()
        repeat = input("Would you like to enter more data? [y/n]: ").lower()
    #if they don't want to repeat, end the main loop
    if repeat == 'n':
        main = False
    #continue nevertheless 
    continue

#displays all the info from the program
print(f"People Processed: {processed:14}\n")
print(f"Not eligible to vote: {not_eligible:10}")
print(f"Eligible but not registered: {not_registered:3}")
print(f"Registered but didn't vote: {not_voted:4}")
print(f"Voted: {voted:25}")







            