import requests


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
            print("Geçersiz para birimi.")
            return None
    else:
        print(f"Hata: {response.status_code} - {response.text}")
        return None


c1 = input(f"Lütfen bir para birimi seçiniz:\n{list_of_currencies}\n").strip().upper()
if c1 not in list_of_currencies:
    print("Geçersiz para birimi. Programdan çıkılıyor.")
    exit()

value_c1 = input("Çevirmek istediğiniz miktar ne kadar?\n")
if not value_c1.replace('.', '', 1).isdigit():
    print("Geçersiz miktar. Lütfen sayısal bir değer girin.")
    exit()

c2 = input(f"Hangi para birimine çevirmek istersiniz?\n{list_of_currencies}\n").strip().upper()
if c2 not in list_of_currencies:
    print("Geçersiz para birimi. Programdan çıkılıyor.")
    exit()


rate = get_exchange_rate(c1, c2)
if rate:
    result = rate * float(value_c1)
    print(f"{value_c1} {c1} = {result:.2f} {c2}.")
