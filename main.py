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
    return render_template('login.html')




@app.route('/login_instagram', methods=['GET', 'POST'])
def login_instagram():
    form = LoginForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        instagramBot.login(username=username, password=password)
        return redirect(url_for('config_bot'))
    return render_template('login_instagram.html', form=form)


@app.route('/config', methods=['GET', 'POST'])
def config_bot():
    form = ScrapperConfigForm()
    if request.method == 'POST':
        instagramBot.findFollowers(
            target_account_url=form.account_url.data,
            number_following_per_hour=form.followers_count.data,
            time_for_each_follow=form.interval_with_follow.data)
        return redirect(url_for('follow_all'))
    return render_template('config.html', form=form)


@app.route('/following')
def follow_all():
    return instagramBot.followAll()


if __name__ == '__main__':
    app.run(debug=True)