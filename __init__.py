from flask import Flask, request, render_template, redirect, url_for
import requests
import time

print('program initiated')

app = Flask(__name__)

url = '127.0.0.1:5000/'

red_pin = 5
green_pin = 6
blue_pin = 13
coffee_pin = 19
amp_pin = 26
ON = 0
OFF = 1  # for some reason relay is backwards, ON or 1 means OFF


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/button', methods=['POST', 'GET'])
def button():
    if request.method == 'POST' or 'GET':
        url_decorator = request.form['submit']
        return redirect(url_for(url_decorator))
    else:
        return render_template('home.html')


@app.route('/red', methods=['GET', 'POST'])
def red():
    print('turning lights red')
    if request.method == 'POST' or request.method == 'GET':
        print('red')
    return 'red'


if __name__ == '__main__':
    app.run()

