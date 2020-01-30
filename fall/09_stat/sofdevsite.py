#Jude Rizzo
#Sofdev1 pd9
#K09 -- ’Tis Not a Race -- But You Will Go Faster
#2019--9--19
from flask import Flask
app = Flask(__name__)
#print("Printing this in the flask console")

#you set a route with the decorator, which is marked by an @
#each one seems to have one fcuntion under it
@app.route("/")
def hello_world():
  print(__name__)
  return  "Call me king, cuz I be k"

 #also every string in the decorator begins with a /

@app.route("/static/template.html")
#in class assignment
def template():
    x = [0,1,1,2,3,5,8]
    return "coll = " + str(x)

@app.route("/../../")
def work():
    return "route 3"

if __name__ == "__main__":
  app.debug = True
  app.run()
