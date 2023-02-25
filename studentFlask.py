from flask import Flask, render_template, redirect, url_for, request
import sys
import DatabaseFlask

app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("mainPage.html")

@app.route('/menuChoice', methods = ['POST','GET'])
def menu():
    # type this url in browser : file:///c:/training/python/github/python/templates/getUserName.html
    # change method to post and get one at a time
    if request.method == 'POST':
        choice = request.form['nm']
        if choice == "1":
            return render_template("studentAdmission.html")
        elif choice == "2":
            return redirect(url_for('select'))
        elif choice == "4":
            sys.exit()

@app.route('/insert', methods = ['POST','GET'])
def insert():
    # type this url in browser : file:///c:/training/python/github/python/templates/getUserName.html
    # change method to post and get one at a time
    if request.method == 'POST':
        record = request.form
        #return "name is " + record['name']
        DatabaseFlask.Database.insert(record['name'], record['age'], record['email'], record['course'], record['active'])
        return redirect(url_for('mainPage'))
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
    return render_template("report.html", hmylist = mylist)
    #return render_template("result.html", result = mydict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
