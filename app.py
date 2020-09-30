from flask import Flask, render_template, flash, request, redirect, jsonify
from forex_python.converter import CurrencyRates
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY']="david-lynch-coffee-7754"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_route():
    return render_template('start.html')


@app.route('/currency', methods=['POST'])
def currency_check():
    origin = request.form['origin']
    travel =request.form['travel']
    amount = request.form['amount']

    # c = CurrencyRates()
    # c.get_rates('origin')

    return render_template('currency.html', origin=origin, travel=travel, amount=amount)
    # return f"""
    # <h1>{origin}{travel}{amount}</h1>
    # """