from flask import Flask
app = Flask(__name__)
#print("Printing this in the flask console")
@app.route("/")
@app.route("/..")
@app.route("/../../")


def hello_world():
  print(__name__)

  return  "1,2,3"



def printStuff():
    return "<header> Here's some valid html </header>"

if __name__ == "__main__":
  app.debug = True
  app.run()
