from flask import Flask,render_template,request,redirect,flash
# https://www.askpython.com/python-modules/flask/flask-flash-method

app = Flask(__name__)
app.secret_key = 'abc123'

@app.route('/form')
def form():
    return render_template('flashform.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        password = request.form['password']
        if password == '123':
            #The following flash message will be displayed on successful login, flash uses session variables, pls define secret key
            flash('Login successful')
            return render_template('flashsuccess.html')
        else:
            return redirect('/form')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
