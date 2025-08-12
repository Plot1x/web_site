from binance.client import Client


api_key = ""
api_secret = ""


client = Client(api_key, api_secret)

def get_crypto_price():
    info = client.get_all_tickers()
    return info
