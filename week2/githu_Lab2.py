#Keenan Githu
#W2D2 Lab 2
#1-22-2025

"""
PROGRAM PROMPT:
You have been asked to produce a report that lists all the computers in the csv file
filehandling.csv.

VARIABLE DICTIONARY:
file - the extracted csv file
record - a list of all the items in a single row
temp_list - list that temporarily stores records to be printed

NOTES:
None
"""


import csv

#open the file
with open('text_files/filehandling.csv') as csvfile:

    #read the file
    file = csv.reader(csvfile)

    #text formatting for columns
    print("Type      Brand   CPU\tRAM   1st Disk  No HDD \t2nd Disk    OS  YR")

    #for each row in the file
    for record in file:

        #create a list for storing stuff to print all at once
        temp_list = []

        #decides between D and L to show which one will be printed
        if record[0] == 'D':
            temp_list.append('Desktop')
        elif record[0] == 'L':
            temp_list.append('Laptop')
        
        #genuine question: why is switch-case called match-case in python? Is switch used somewhere else in Python, or am I just wrong?
        #switch case for manufacturer
        match record[1]:
            case 'DL':
                temp_list.append('Dell')
            case 'HP':
                temp_list.append('HP')
            case 'GW':
                temp_list.append('Gateway')
        
        #I didn't want to spam append
        temp_list.extend(record[2:6])
        
        #all the ridiculous formatting mumbo jumbo for printing properly
        #if there's only 1 hard drive
        if record[5] == '1':
            temp_list.extend(record[6:8])
            print(f"{temp_list[0]:<7}   {temp_list[1]:<8}{temp_list[2]} \t{temp_list[3]}    {temp_list[4]} \t {temp_list[5]} \t \t   {temp_list[6]}  {temp_list[7]}")
        
        #if there's two
        elif record[5] == '2':
            temp_list.extend(record[6:9])
            print(f"{temp_list[0]:<7}   {temp_list[1]:<4}    {temp_list[2]} \t{temp_list[3]}    {temp_list[4]} \t {temp_list[5]} \t {temp_list[6]} \t   {temp_list[7]}  {temp_list[8]}")