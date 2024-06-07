from flask import Flask, jsonify, render_template
from foods import foods

app = Flask(__name__)

app.config['DEBUG'] = False

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
    age = 66
    isWelcome = False
    return render_template('options.html', name=name, isWelcome=isWelcome, age=age)

@app.route('/foods', methods=['GET'])
def foodsdisplay():
    return render_template('foods.html', foods=foods)

@app.route('/calculate/add/<int:a>/<int:b>')
def add(a,b):
    c = str(a+b)
    return c

@app.route('/calculate/divide/<int:a>/<int:b>')
def divide(a,b):
    c = str(a/b)
    return c

if __name__ == '__main__':
    app.run()