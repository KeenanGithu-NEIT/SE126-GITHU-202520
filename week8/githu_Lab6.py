#Keenan Githu
#W8D1 Lab 6
#2-24-2025

"""
PROGRAM PROMPT:


VARIABLE DICTIONARY:

NOTES:
None
"""

#prints the seating chart
def print_seating(seating):
    print("ROW")

    for i in range(len(seating)):
        print(f" {seating[i][0]}  {seating[i][1]} {seating[i][2]}    {seating[i][3]} {seating[i][4]}")

#function to ask if they want to continue
def askToContinue(more):

    while more == True:
        add_more = input("Would you like to add more seats? (y/n): ")
        if add_more == "y":
            return more
        
        elif add_more == "n":
            more = False
            return more
        
        else:
            print("\nInvalid input\n")
            continue

#plane seats 2d list
plane_seats = [
    [1, 'A', 'B', 'C', 'D'],
    [2, 'A', 'B', 'C', 'D'],
    [3, 'A', 'B', 'C', 'D'],
    [4, 'A', 'B', 'C', 'D'],
    [5, 'A', 'B', 'C', 'D'],
    [6, 'A', 'B', 'C', 'D'],
    [7, 'A', 'B', 'C', 'D']
]

#loop start
choosing = True

while choosing == True:

    #print seats
    print_seating(plane_seats)

    choose_seat = input("Choose a seat (ex. D7 or B4): ")

    #list out the input
    search = list(choose_seat)

    #if it's less than or greater than 2, loops back to start
    if len(search) > 2 or len(search) < 2:
        print("\nInvalid Input\n")
        continue
    
    #if there's an invalid letter in first position, loops back to start
    if search[0] != "A" and search[0] != "B" and search[0] != "C" and search[0] != "D":
        print("\nInvalid Input\n")
        continue
    
    #makes sure that second position has a number
    try:
        search[1] = int(search[1])

    except:
        print("\nInvalid Input\n")
        continue

    #checks if it's a valid number
    if search[1] < 1 and search[1] > 7:
        print("\nInvalid Input\n")
        continue

    #loops through lists to find correct one
    for i in plane_seats:
        #once it finds it
        if i[0] == search[1]:
            #makes the position in the list an X
            try:
                location = i.index(search[0])
                i[location] = "X"
            #if the spot is already taken
            except:
                print("\nSeat already taken.\n")
    
    #function call asking to continue
    if askToContinue(choosing) == False:
        choosing = False
