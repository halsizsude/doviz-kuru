from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '52ef80f97d1737e2f1e4b023'
BASE_URL = 'https://v6.exchangerate-api.com/v6'

list_of_currencies = [
    "USD", "EUR", "GBP", "ILS", "DKK", "CAD", "IDR", "BGN",
    "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD",
    "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "LTL",
    "NOK", "RUB", "INR", "MXN", "CZK", "BRL", "PLN", "PHP", "ZAR"
]

def get_exchange_rate(c1, c2):
    url = f"{BASE_URL}/{API_KEY}/latest/{c1}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data['conversion_rates'].get(c2)
        if rate:
            return rate
        else:
            return None
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        c1 = request.form.get('from_currency')
        c2 = request.form.get('to_currency')
        value_c1 = request.form.get('amount')

        if c1 in list_of_currencies and c2 in list_of_currencies and value_c1.replace('.', '', 1).isdigit():
            rate = get_exchange_rate(c1, c2)
            if rate:
                result = round(float(value_c1) * rate, 2)
            else:
                result = "Geçersiz para birimi veya API hatası."
        else:
            result = "Lütfen geçerli bilgileri girin."

    return render_template('index.html', currencies=list_of_currencies, result=result)

if __name__ == '__main__':
    app.run(debug=True)
