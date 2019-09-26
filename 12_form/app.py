
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def functions():
    return render_template(
    'form.html'
    )

@app.route("/auth")
def authenticate():
    #print(app)
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #print(request)
    #print("22222!!")
    #print(request.args)
    print(1111)
    print(request.headers)
    print(1111)
    return render_template(
    'submited.html'
    )





if __name__ == "__main__":
  app.debug = True
  #run the main code
  app.run()
