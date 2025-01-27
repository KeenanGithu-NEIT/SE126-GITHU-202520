#Keenan Githu
#W4D1 Lab 3
#1-27-2025

"""
PROGRAM PROMPT:
Rewrite the Voter Registration Lab utilizing the data from the file voters.csv. 
Store the field data into respective 1D lists, and then process the lists to determine 
the 4 final output values (make sure they are clearly labeled!). This final solution 
should have NO input() statements and when the console is ran it should print all 4 
totals (you may reprint the data from the lists/fie if you would like)  Use your original 
Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a 
file and store data into lists, then use a for loop to process each voter and their data to find the 4 totals.

VARIABLE DICTIONARY:
total_records   total number of records processed
cant_register   number of people who can't register
not_registered  number of people who can register, but didn't
didnt_vote      number of people who registered, but didn't vote
voted           number of people who voted

NOTES:
None

"""
import csv

voter_information = {
    'ID Number': [],
    'Age': [],
    'Registered': [],
    'Voted': []
}

total_records = 0
cant_register = 0
not_registered = 0
didnt_vote = 0
voted = 0

#open the file
with open('text_files/voters_202040.csv') as csvfile:

    #read it
    file = csv.reader(csvfile)

    #stores all the file information into lists
    for record in file:
        voter_information['ID Number'].append(record[0])
        voter_information['Age'].append(int(record[1]))
        voter_information['Registered'].append(record[2])
        voter_information['Voted'].append(record[3])
    
    #the total of all records processed
    total_records = len(voter_information['ID Number'])

    #counts the people who cant register to vote
    for i in voter_information['Age']:
        if i < 18:
            cant_register += 1
    
    #counts the people who didn't register
    for i in voter_information['Registered']:
        if i == 'N':
            not_registered += 1
    
    #subtracts the people who can't register whatsoever
    not_registered -= cant_register
    
    #counts the people who did or didn't vote
    for i in voter_information['Voted']:
        if i == 'N':
            didnt_vote += 1
        elif i == 'Y':
            voted += 1

    #subtracts the people who didn't register and the people who can't register
    didnt_vote -= not_registered + cant_register

    #print all the numbers
    print(f"Total Records Processed: {total_records}\n")
    print(f"Number of people not eligible to register: {cant_register}")
    print(f"Number of people who can register but aren't: {not_registered}")
    print(f"Number of people who registered but didn't vote: {didnt_vote}")
    print(f"Number of people who did vote: {voted}")
    
