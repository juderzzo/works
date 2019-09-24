# Jude Rizzo
# SoftDev1 pd9
# K10: Jinja Tuning
# 2019-09-24

# Pair Programming
# Team Name: Red Notebook
# Roster: Brandon Chen, Jude Rizzo


from flask import Flask, render_template
#importing the libraries
import random, csv
app = Flask(__name__)

allOccupation = {}

def randomOccupation():
    with open('occupations.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        linenum = 0
        #seperated by commas, so we tell them by their "delimeter"
        for rows in reader:
            if linenum != 0:
                #associating the percentages in the csv
                allOccupation[rows[0]] = (float(rows[1]),rows[2])
                print(allOccupation)
            linenum += 1
        counter = 0

        randomnum = random.uniform(0,99.8)
        #picks a number from 0 to 99.8, and we will see which number
        #in the percentages it lands on with resepct to jobs

        for key, value in allOccupation.items():
            counter += value[0]
            #now, think o this as going around a pie chart until we reach the desired number
            if randomnum <= counter:
                return key




@app.route("/occupyflaskst")
def getAJob():

    return render_template(
    #set itup with the template
        'template.html',
        randOccup = randomOccupation(),
        bunch = allOccupation

    )


if __name__ == "__main__":
  app.debug = True
  #run the main code
  app.run()
