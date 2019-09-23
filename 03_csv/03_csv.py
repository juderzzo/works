import csv
import random
occs = {}
chooser = []

with open('occupations.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if(row[1] != 'Percentage' and row[0] != 'Total'):
            occs[row[0]] = float(row[1])
            for  i in range(int(float(row[1]) *10) - 1):

                chooser.append(row[0])

print(chooser)
print(random.choice(chooser))
