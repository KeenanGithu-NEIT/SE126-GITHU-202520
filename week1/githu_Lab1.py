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

def intConvert(convert_value):
    try:
        convert_value = int(convert_value)
        return convert_value
    except:
        return False

def difference(people, max_cap):
    total = max_cap - people
    return total

def decision(response):
    if response == 'y':
        return True
    elif response == 'n':
        return False
    else:
        print("\nInvalid Input\n")
        return "Error"
    

run = True

while run == True:

    again = 'a'

    meeting_name = input("\nWhat is the name of the meeting?: ")

    people = input("\nHow many people will be attending the meeting?: ")
    while intConvert(people) == False:
        print("\nInvalid Input\n")
        people = input("How many people will be attending the meeting?: ")
    people = intConvert(people)

    max_cap = input("\nWhat is the maximum room capacity?: ")
    while intConvert(max_cap) == False:
        print("\nInvalid Input\n")
        max_cap = input("What is the maximum room capacity?: ")
    max_cap = intConvert(max_cap)

    total = difference(people, max_cap)
    if total > 0:
        print(f"\nYou can fit {total} more people in the meeting.")
    else:
        print(f"\nThere's too many people in the meeting. Please lower the amount of attendants by {total*-1} people.")

    while decision(again) == "Error":
        again = input("\nWould you like to add another meeting? [y/n]: ").lower()
    run = decision(again)
    continue
