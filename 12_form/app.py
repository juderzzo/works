# Jude Rizzo
# SoftDev1 pd9
# K12: Echo Echo Echo
# 2019-09-24

# Pair Programming
# Team Name: Keyboard
# Roster: Henry Liu, Jude Rizzo
from flask import Flask
from flask import render_template
from flask import request
#imports
app = Flask(__name__)

@app.route("/")
def functions():
    return render_template(
    'form.html'
    )

##link the starting page to the template, then connect it
#to the form

@app.route("/auth")
def authenticate():
    #print(app)
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #print(request)
    #print("22222!!")
    #print(request.args)
    #print(1111)
    print(request.headers)
    #print(1111)
    return render_template(
    'submited.html'
    )

    #when yuo get redireccted to auth, them show the submitted
    #the submiteed has python on it to show the username





if __name__ == "__main__":
  app.debug = True
  #run the main code
  app.run()
