#Keenan Githu
#W3D2 Class Lab 3
#1-23-2025

"""
PROGRAM PROMPT:
Your CIO (Chief Information Officer) has asked you to determine how much it would cost 
the company to replace all machines that are from 2016 and earlier. He plans on spending 
not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the 
file lab3a.csv into lists.  Then process the lists to reprint all of the file information 
(exactly as you did in Lab 2) and also produce an end report that lists the number of desktops 
that will be replaced, the cost to replace the desktops, the number of laptops that will be 
replaced, and the cost to replace the laptops.

VARIABLE DICTIONARY:
computer_stuff - dictionary for lists
counting - counts each computer, later used to print lists
double_storage_counter - counts each computer with two hard drives, later used to print lists
laptops_replace - laptops that need to be replaced


NOTES:
There's lists in the dictionary, I think it counts.
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

#pile of counting variables
counting = 0
double_storage_counter = 0

#pile of computers to replace
laptops_replace = 0
desktops_replace = 0

#open the file
with open('text_files/filehandling-1.csv') as csvfile:

    #read it
    file = csv.reader(csvfile)

    #column formatting
    print("Type      Brand   CPU\tRAM   1st Disk  No HDD \t2nd Disk    OS  YR")

    #for each row in the file
    for record in file:

        """I pasted most of the same code I wrote in Lab 2, if it works, it works."""
        
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
        
        #if there's one hard drive
        if record[5] == '1':
            computer_stuff[8].append(record[6])
            computer_stuff[9].append(record[7])
            
            #if the computer is from 2016 or older
            if int(record[7]) <= 16:
                #if it's a desktop
                if record[0] == 'D':
                    desktops_replace += 1
                #if it's a laptop
                elif record[0] == 'L':
                    laptops_replace += 1

            #a weird print statement
            print(f"{computer_stuff[1][counting]:<7}   {computer_stuff[2][counting]:<8}{computer_stuff[3][counting]} \t{computer_stuff[4][counting]}    {computer_stuff[5][counting]} \t {computer_stuff[6][counting]}       \t   {computer_stuff[8][counting]}  {computer_stuff[9][counting]}")

        #if there's two hard drives
        if record[5] == '2':
            for x in range(6, 9):
                computer_stuff[x+1].append(record[x])
            
            #if the computer is from 2016 or older
            if int(record[8]) <= 16:
                #if it's a desktop
                if record[0] == 'D':
                    desktops_replace += 1
                #if it's a laptop
                elif record[0] == 'L':
                    laptops_replace += 1

            #weirder print statement
            print(f"{computer_stuff[1][counting]:<7}   {computer_stuff[2][counting]:<8}{computer_stuff[3][counting]} \t{computer_stuff[4][counting]}    {computer_stuff[5][counting]} \t {computer_stuff[6][counting]}       {computer_stuff[7][double_storage_counter]}\t   {computer_stuff[8][counting]}  {computer_stuff[9][counting]}")
            #increments the counter for double_storage_counter
            double_storage_counter += 1

        #increments the counting variable no matter what
        counting += 1
    
    #final numbers to print
    print(f"\n\n\nThe cost for replacing {desktops_replace} desktops is: ${desktops_replace*2000}")
    print(f"The cost for replacing {laptops_replace} laptops is: ${laptops_replace*1500}")