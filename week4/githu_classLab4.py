import csv

first_names = []
last_names = []
test1_grades = []
test2_grades = []
test3_grades = []

with open("text_files/class_grades-2.csv") as csvfile:

    file = csv.reader(csvfile)

    for record in file:
        
        first_names.append(record[0])
        last_names.append(record[1])
        test1_grades.append(record[2])
        test2_grades.append(record[3])
        test3_grades.append(record[4])

        average_grade = (int(record[2]) + int(record[3]) + int(record[4]))/3

        print(average_grade)



