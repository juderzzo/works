#Jude Rizzo
#Sofdev1 pd9
#K06 -- Divine your Destiny!
#2019--9--17
import csv
import random

#well need to import csv to use a reader
occs = {}
chooser = []
#set up some dictionaries and lists we'll use later
with open('occupations.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #this splits up each line by comma, as our file is,
    #and sstroes them erach by rows, which are lists of 2 elemetns
    for row in reader:
        if(row[1] != 'Percentage' and row[0] != 'Total'):
            #the top columns is just explaining what the csbv is so we don't need it
            occs[row[0]] = float(row[1])
            #make a
            for  i in range(int(float(row[1]) *10) - 1):
                #in order to get an integer representation, we
                #make a list of 1000 elements, and give each occupation
                #it's percentage of 1000 according to the csv file
                chooser.append(row[0])

print(chooser)
print(random.choice(chooser))
#now we randomly choose from this list an occupation
