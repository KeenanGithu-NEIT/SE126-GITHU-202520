










def intConvert(convert_value):
    try:
        convert_value = int(convert_value)
        return convert_value
    except:
        return False

def difference(people, max_cap):
    total = max_cap - people
    return total


run = True

while run == True:
    people = input("How many people will be attending the meeting?: ")
    while intConvert(people) == False:
        print("\nInvalid Input\n")
        people = input("How many people will be attending the meeting?: ")
    people = intConvert(people)

    max_cap = input("What is the maximum room capacity?: ")
    while intConvert(max_cap) == False:
        print("\nInvalid Input\n")
        max_cap = input("What is the maximum room capacity?: ")
    max_cap = intConvert(max_cap)

    total = difference(people, max_cap)
    if total > 0:
        print(f"You can fit {total} more people in the meeting.")
    else:
        print(f"There's too many people in the meeting. Please lower the amount of attendants by {total} people.")

    again = input("Would you like to run the program again? [y/n]: ")
    
