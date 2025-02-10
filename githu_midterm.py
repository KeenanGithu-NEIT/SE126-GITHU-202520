import csv
import random

#variable used for a later loop
search = True

#lists for storing pre-existing data
first_name = []
last_name = []
email = []
department = []
phone_extensions = []

#list for data being created within the program
office_numbers = []

#2D list to store values for later writing
write_to_new_file = []

#function for assigning office numbers
def assignOfficeNumber():
    #randomize number, if it's already taken, redo it until it hits one that isn't
    office_number = random.randint(100,200)
    while office_numbers.count(office_number) == 1:
        office_number = random.randint(100,200)

    #append and return the value
    office_numbers.append(office_number)

    return office_number

#opening the file
with open('text_files/westeros.csv') as csvfile:

    #convert
    file = csv.reader(csvfile)

    #reading
    for record in file:
        
        #in case a line is blank
        if len(record) == 0:
            continue
        
        #grab all info from record
        first_name.append(record[0])
        last_name.append(record[1])
        email.append(record[2])
        department.append(record[3])
        phone_extensions.append(record[4])

        #store all the stuff to be written later
        #also use the opportunity to assign the office number (only reason why the number was returned)
        write_to_new_file.append([record[0], record[1], record[2], record[3], record[4], assignOfficeNumber()])

#formatting for printing
print("FIRST     LAST  \t EMAIL\t \t \t \t DEPARTMENT\t \t  EXT   OFFICE #")

#print all the stuff
for i in range(len(first_name)):
    print(f"{first_name[i]:10}{last_name[i]:15}{email[i]:32}{department[i]:25}{phone_extensions[i]:7}{office_numbers[i]}")

#open other file in write mode
with open('text_files/midterm_choice1.csv', 'w', newline='') as csvfile:

    #convert
    file = csv.writer(csvfile)

    #write all the rows to the new csv at once
    file.writerows(write_to_new_file)

#previously mentioned loop
while search == True:
    
    #prompt
    print("\nWesteros Services Directory Search")
    print("1. Search By EMAIL")
    print("2. Search By DEPARTMENT")
    print("3. EXIT\n")

    #input
    option = input("Choose a search option from the list above (1-3): ")

    #if the input is invalid
    if option != "1" and option != "2" and option != "3":
        print("\nNot a valid option.\n")
        continue
    
    #Search By EMAIL
    if option == "1":
        email_input = input("Enter the Email: ")

        #if the email doesn't exist
        if email.count(email_input) == 0:
            print("\nUser Not Found\n")
            continue

        #if the user does exist, show all their data
        else:
            print(f"\n{first_name[email.index(email_input)]}")
            print(last_name[email.index(email_input)])
            print(email_input)
            print(department[email.index(email_input)])
            print(phone_extensions[email.index(email_input)])
            print(office_numbers[email.index(email_input)])
    
    #Search By DEPARTMENT
    if option == "2":
        department_input = input("Enter the Department: ")

        #if the department doesn't exist
        if department.count(department_input) == 0:
            print("\nUser Not Found\n")
            continue

        #if it does, print the data of everyone in said department
        else:
            for i in range(len(department)):
                if department[i] == department_input:
                    print()
                    print(first_name[i])
                    print(last_name[i])
                    print(email[i])
                    print(department_input)
                    print(phone_extensions[i])
                    print(office_numbers[i])
                    print()

    #EXIT
    if option == "3":
        search = False
        continue