#Keenan Githu
#W3D2 Class Lab 3
#1-23-2025

"""
PROGRAM PROMPT:

VARIABLE DICTIONARY:


NOTES:

"""
import csv

#the magic of dictionaries :D
computer_stuff = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
}

counting = 0
double_storage_counter = 0

with open('text_files/filehandling-1.csv') as csvfile:

    file = csv.reader(csvfile)

    print("Type      Brand   CPU\tRAM   1st Disk  No HDD \t2nd Disk    OS  YR")

    for record in file:

        """I pasted the same code I wrote in Lab 2, if it works, it works."""
        
        #decides between D and L to show which one will be printed
        if record[0] == 'D':
            computer_stuff[1].append('Desktop')
        elif record[0] == 'L':
            computer_stuff[1].append('Laptop')
        
        #switch case for manufacturer
        match record[1]:
            case 'DL':
                computer_stuff[2].append('Dell')
            case 'HP':
                computer_stuff[2].append('HP')
            case 'GW':
                computer_stuff[2].append('Gateway')
        
        #I still refuse to spam append
        for i in range(2, 6):
            computer_stuff[i+1].append(record[i])
        
        if record[5] == '1':
            computer_stuff[8].append(record[6])
            computer_stuff[9].append(record[7])

        if record[5] == '2':
            for x in range(6, 9):
                computer_stuff[x+1].append(record[x])
            print(f"{computer_stuff[1][counting]:<7}   {computer_stuff[2][counting]:<8}{computer_stuff[3][counting]} \t{computer_stuff[4][counting]}    {computer_stuff[5][counting]} \t {computer_stuff[6][counting]}       {computer_stuff[7][double_storage_counter]}\t   {computer_stuff[8][counting]} {computer_stuff[9][counting]}")
            double_storage_counter += 1

        counting += 1