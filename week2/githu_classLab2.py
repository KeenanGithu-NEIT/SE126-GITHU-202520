import csv

over_capacity = []

with open('week2/text_files/classLab2.csv') as csvfile:

    file = csv.reader(csvfile)

    for record in file:
        record[1] = int(record[1])
        record[2] = int(record[2])
        if record[1] - record[2] < 0:
            over_capacity.append(f"{record[0]}.{record[1] - record[2]}")
    
    for record in file:
        over_capacity[0].split(".")
        print(over_capacity[0])
