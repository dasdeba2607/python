from flask import Flask, render_template, abort
# https://www.digitalocean.com/community/tutorials/how-to-handle-errors-in-a-flask-application

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', lname = "Deba" ), 404


@app.route('/')
def index():
    return render_template('errorindex.html')


@app.route('/messages/<int:idx>')
def message(idx):
    app.logger.info('Building the messages list...')
    messages = ['Message Zero', 'Message One', 'Message Two']
    try:
        app.logger.debug('Get message with index: {}'.format(idx))
        return render_template('message.html', message=messages[idx])
    except IndexError as e:
        app.logger.error('Index {} is causing an IndexError'.format(idx))
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
