from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/goldenbell')
def goldenbell():
    return render_template('goldenbell.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/dictionary')
def dictionary():
    return render_template('dictionary.html')

@app.route('/goods')
def goods():
    return render_template('goods.html')

if __name__ == '__main__':
    app.run(debug=True)
