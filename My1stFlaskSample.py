from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


# @app.route("/hello1") ## decorator example with path
def hello1():
    return render_template("sample.html", mydate=datetime.datetime.now())

app.add_url_rule('/deba', '', hello1)  ## decorator example with path

@app.route("/<int:myno>")  ## decorator example with int
def PrintFloat(myno):
    return "Myno is :" + str(myno)

@app.route("/<float:myfloat>") ## decorator example with path
def PrintNumber(myfloat):
    return "Myfloat is :" + str(myfloat)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)


