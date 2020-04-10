import csv

with open('sprint1.txt', 'r') as file:
    data = []
    student = []
    for index, line in enumerate(file):
        if index % 12 == 0:
            data.append(student)
            student = []
        student.append(line.strip())
    data.append(student)

with open('sprint1.csv', 'w+', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    for student in data:
        writer.writerow(student)