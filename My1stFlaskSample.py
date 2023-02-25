from flask import Flask, render_template, redirect, url_for, request
import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>You are on home page!</h1>"


# @app.route("/hello1") ## decorator example with path
def hello1():
    return render_template("sample.html", mydate=datetime.datetime.now())


app.add_url_rule('/deba', '', hello1)  ## decorator example with path


@app.route("/<int:myno>")  ## decorator example with int
def PrintFloat(myno):
    return "Myno is :" + str(myno)


@app.route("/<float:myfloat>")  ## decorator example with path
def PrintNumber(myfloat):
    return "Myfloat is :" + str(myfloat)

@app.route('/user/<username>')
def displayUser(username):
    # this html contains css and css is served from /static endpoint, so css file has to be under /static subfolder under python script folder
    return render_template("userValidationwithCSS.html", user = username)
    """
    if username == "admin":
        return "Welcome Admin " + username
    else:
        return "Welcome user " + username
    """

@app.route('/checkUser/<username>')
def validateUser(username):
    return redirect(url_for('displayUser', username = username))

@app.route('/login', methods = ['POST','GET'])
def getLoginData():
    # type this url in browser : file:///c:/training/python/github/python/templates/getUserName.html
    # change method to post and get one at a time
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('displayUser', username = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('displayUser', username = user))

@app.route('/userForm')
def displayUserForm():
    # instead of typing file:///c:/training/python/github/python/templates/getUserName.html, please hit this endpoint
    return render_template('getUserName.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
