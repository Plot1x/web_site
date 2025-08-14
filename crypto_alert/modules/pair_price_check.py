from binance.client import Client


api_key = ""
api_secret = ""


client = Client(api_key, api_secret)

def get_crypto_price():
    info = client.get_all_tickers()
    return info

def get_all_crypto_symbol():
    arr = []
    info = get_crypto_price()
    for i in info:
        arr.append(i['symbol'])
    return arr
