#Keenan Githu
#W2D1 Class Lab 2
#1-13-2025

"""
PROGRAM PROMPT:
Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

VARIABLE DICTIONARY:
file_count      counts the amount of files processed
over_capacity   stores the information for the rooms over capacity
over_limit      counts the rooms over the limit
file            reference file to loop through
temp_list       temporary list that keeps the first element of the list on each loop

NOTES:
The formatting for over_capacity elements is given an example below (did that sentence make sense?):
'Federation.50'
Federation is the name of the room, while 50 is the number of people who need to be put on the wait list.
"""

import csv

#counts files processed
file_count = 0
#storage for rooms over capacity
over_capacity = []
#count for the rooms over the limit
over_limit = 0

#open the file
with open('text_files/classLab2.csv') as csvfile:

    #read it
    file = csv.reader(csvfile)

    #formatting for header
    print("Room Name \t \t Max People    People Attending")
    print("---------------------------------------------------------")

    #loops for each record in file
    for record in file:
        file_count += 1
        #converts numbers to integers
        record[1] = int(record[1])
        record[2] = int(record[2])
        #if the max is smaller than the people attending, puts its information in over_capacity and adds 1 to over_limit count
        if record[1] - record[2] < 0:
            over_capacity.append(f"{record[0]}.{record[2]-record[1]}")
            over_limit += 1
        #printing for all the numbers
        print(f"{record[0]:20} {record[1]:10.0f} {record[2]:15.0f}")

    #goes through each item in over_capacity
    for i in over_capacity:
        #splits first element of list
        temp_list = over_capacity[0].split(".")
        print("---------------------------------------------------------")
        print("\n\t!\tProblem Found\t!\n")
        print(f"{temp_list[0]} has too many people. {temp_list[1]} people will have to be on the wait list.\n")

        #removes first element
        over_capacity.pop(0)

    #forcing the last instance of the list (I'm tired)
    temp_list = over_capacity[0].split(".")
    print("---------------------------------------------------------")
    print("\n\t!\tProblem Found\t!\n")
    print(f"{temp_list[0]} has too many people. {temp_list[1]} people will have to be on the wait list.\n")
    over_capacity.pop(0)
    print("---------------------------------------------------------")

    #printing out record counts
    print(f"\nProcessed {file_count} records.")
    print(f"There are {over_limit} rooms over the limit.")