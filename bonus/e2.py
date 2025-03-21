import csv

with open('../weather.csv','r') as file:
    data = list(csv.reader(file))


City = input("Enter a city: ")

for row in data:
    if row[0] == City:
        print(row[1])

