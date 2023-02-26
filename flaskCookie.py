from flask import Flask, render_template, request, make_response

app = Flask(__name__)

allowed_paths = ['/setcookie', '/getcookie', '/static/styles.css', '/']
allowed_methods = ['GET', 'POST']

@app.route('/')
def index():
   return render_template('cookieindex.html')


@app.route('/setcookie', methods = ['POST'])
def setcookie():
   if request.method == 'POST':
       user = request.form['userid']

       resp = make_response(render_template('readcookierequest.html'))
       resp.set_cookie('userID', user)

       return resp

@app.route('/getcookie')
def getcookie():
    if request.method == 'GET':   ## if we don't specify anything about method in html file, it will be always GET method
        name = request.cookies.get('userID')
        #response.delete_cookie('userID')
        return '<h1>welcome '+name+'</h1>'

@app.before_request  ## https://instructobit.com/tutorial/111/Python-Flask%3A-running-code-before-and-after-every-request
def before_request_callback():
    path = request.path
    root = request.script_root
    #print("path " + path)
    #print("root " + root)
    if path not in allowed_paths:
        print("invalid path")
        return render_template('invalidpath.html')
    method = request.method
    if method not in allowed_methods:
        print("invalid method")
        return render_template('invalidmethod.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
