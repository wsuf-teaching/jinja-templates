from flask import Flask, jsonify, render_template, request, redirect, url_for
from foods import foods

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/templateparams')
def templateparams():
    food =     {
        'name': 'Pizza',
        'price': 10.99,
        'description': 'A delicious Italian dish'
    }
    return render_template('templateparams.html', name='John Doe', age=20, food=food)

@app.route('/templateparams2/<string:name>')
def templateparams2(name):
    return render_template('templateparams2.html', displayname=name)

@app.route('/options')
def options():
    name = "John Doe"
    age = 14
    isWelcome = True
    return render_template('options.html', name=name, isWelcome=isWelcome, age=age)

@app.route('/foods', methods=['GET'])
def foodsdisplay():
    return render_template('foods.html', foods=foods)

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/theform', methods=['GET','POST'])
def theform():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        location = request.form['location']
        # do some calculation with the name and location
        # name = ....
        # and redirect the user to somewhere
        return redirect(url_for('index'))
        #return 'Hello {}. You are from {}. You have submitted the form successfully.'.format(name, location)

if __name__ == '__main__':
    app.run()