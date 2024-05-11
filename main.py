from flask import Flask, render_template, redirect, url_for, request, flash
from form import LoginForm, ScrapperConfigForm
from flask_bootstrap import Bootstrap5
from instagrambotmvp import InstaFollower
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def home():
    global instagramBot
    instagramBot = InstaFollower()
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        instagramBot.login(username=username, password=password)
        return redirect(url_for('config'))
    return render_template('login.html', form=form)


@app.route('/config')
def config():
    form = ScrapperConfigForm()
    return render_template('config.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)