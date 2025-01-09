#Keenan Githu
#W1D2 Lab 1
#1-9-2025

"""
PROGRAM PROMPT:
A program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The
program will accept the maximum room capacity and the number of people attending the meeting. 
If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and 
tells how many additional people may legally attend.  If the number of people exceeds the maximum room capacity, the program
announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. 
The user should be allowed to enter and check as many rooms as they would like without exiting the program.

VARIABLE DICTIONARY:
convert_value   parameter to convert into an integer the intConvert function
run             looping code for main program
again           will determine if the program should repeat
people          amount of people attending meeting
max_cap         maximum amount of people allowed in one room
total           the difference of max_cap and people
"""

#converts two of the inputs to integers 
def intConvert(convert_value):

    try:
        convert_value = int(convert_value)
        return convert_value

    except:
        return False

#gets difference between max_cap and people
def difference(people, max_cap):
    total = max_cap - people
    return total

#gets decision from again variable, repeats input for again variable if response isn't y or n
def decision(response):

    #normal stuff
    if response == 'y':
        return True
    elif response == 'n':
        return False
    
    #error
    else:
        print("\nInvalid Input\n")
        return "Error"
    
#establish looping variable
run = True

while run == True:

    #resets again to this, will always force the loop at the end to start
    again = 'a'

    #get meeting name
    meeting_name = input("\nWhat is the name of the meeting?: ")

    #get the amount of people
    people = input("\nHow many people will be attending the meeting?: ")

    #try to convert to integer, runs this if it can't
    while intConvert(people) == False:
        print("\nInvalid Input\n")
        people = input("How many people will be attending the meeting?: ")

    #only works if the people variable is a valid convert to integer
    people = intConvert(people)

    #gets maximum amount of people in a room
    max_cap = input("\nWhat is the maximum room capacity?: ")

    #try to convert to integer, runs this if it can't
    while intConvert(max_cap) == False:
        print("\nInvalid Input\n")
        max_cap = input("What is the maximum room capacity?: ")

    #only works if the max_cap variable is a valid convert to integer
    max_cap = intConvert(max_cap)

    #gets difference of max_cap and people, stores to total
    total = difference(people, max_cap)

    #if the total is greater than 0, tells the user how many more people can fit in the meeting room
    if total > 0:
        print(f"\nYou can fit {total} more people in the meeting.")
    #if total is negative
    else:
        print(f"\nThere's too many people in the meeting. Please lower the amount of attendants by {total*-1} people.")

    #this will activate each loop of the main program, since again isn't a valid answer
    while decision(again) == "Error":
        again = input("\nWould you like to add another meeting? [y/n]: ").lower()

    #only runs if decision(again) CANNOT result in "Error"
    #assigns either True or False
    run = decision(again)

    continue
