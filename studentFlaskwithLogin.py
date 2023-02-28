from flask import Flask, render_template, redirect, url_for, request, session, flash
import DatabaseFlask

app = Flask(__name__)
app.secret_key = 'abc123'

@app.route('/')
def index():
    print(session)
    if 'username' in session:
        return render_template("mainPage.html")
    else:
        return render_template("loginpage.html")

@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username == '':
            error = 'Invalid username . Please try again!'
            return render_template("loginpage.html", error = error)
        session['username'] = username
        flash('You were successfully logged in')
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   print("logging out")
   if 'username' in session:
       session.pop('username', None)
       return render_template("loginpage.html")

@app.route('/menuChoice', methods = ['POST','GET'])
def menu():
    # type this url in browser : file:///c:/training/python/github/python/templates/getUserName.html
    # change method to post and get one at a time
    print(session)
    if request.method == 'POST':
        choice = request.form['nm']
        if choice == "1":
            return render_template("studentAdmission.html")
        elif choice == "2":
            return redirect(url_for('select'))
        elif choice == "4":
            return redirect(url_for('logout'))

@app.route('/insert', methods = ['POST','GET'])
def insert():
    # type this url in browser : file:///c:/training/python/github/python/templates/getUserName.html
    # change method to post and get one at a time
    if request.method == 'POST':
        record = request.form
        #return "name is " + record['name']
        DatabaseFlask.Database.insert(record['name'], record['age'], record['email'], record['course'], record['active'])
        return redirect(url_for('index'))
        #return render_template("result.html", result = record)  # this is to pass dictionary item to html

@app.route('/select')
def select():
    recordList = DatabaseFlask.Database.select()
    mylist = []
    for i in recordList:
        count=0
        mydict = {}
        for i in i.split(','):
            if count == 0:
                mydict['Name'] = i
            elif count == 1:
                mydict['Age'] = i
            elif count == 2:
                mydict['Email'] = i
            elif count == 3:
                mydict['Course'] = i
            elif count == 4:
                mydict['Status'] = i
            count+=1
        mylist.append(mydict)
    print(session)
    return render_template("report.html", hmylist = mylist)
    #return render_template("result.html", result = mydict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
