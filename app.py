from flask import Flask, render_template, flash, request, redirect
from forex_python.converter import CurrencyRates, CurrencyCodes
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY']="david-lynch-coffee-7754"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_route():
    return render_template('start.html')


@app.route('/currency', methods=['POST'])
def currency_check():
    source = ['GBP', 'HKD' 'IDR', 'ILS', 'DKK', 'INR', 'CHF','MXN', 'CZK', 'SGD', 'THB', 'THB', 'HRK', 'EUR', 'MYR', 'NOK', 'CNY', 'BGN', 'PHP', 'PLN', 'ZAR','CAD', 'ISK', 'BRL', 'RON', 'NZD','TRY','JPY', 'RUB', 'KRW', 'USD', 'AUD', 'HUF', 'SEK']
    origin = request.form['origin']
    travel =request.form['travel']
    amount = int(request.form['amount'])
    # print(origin in source)
    # print(origin)
    # print(type(origin))
    if origin in source == False:
        flash('origin not valid')
        
        return redirect('/')
    elif travel in origin == False:
        flash('travel not valid')
        return redirect('/')
    else:
        c = CurrencyRates()
        currency_change = c.get_rates(origin)[travel]
        currency_final = currency_change * amount
        # print(currency_change)
        # print(type(currency_change))
        # print(amount)
        # print(type(amount))
        c_code = CurrencyCodes()
        currency_code = c_code.get_symbol(travel)
        return render_template('currency.html', origin=origin, travel=travel, amount=amount, currency_code = currency_code, currency_final = currency_final)



