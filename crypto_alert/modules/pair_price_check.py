from binance.client import Client


api_key = ""
api_secret = ""


client = Client(api_key, api_secret)

def get_crypto_price(symbol1):
    info = client.get_symbol_ticker(symbol=symbol1)
    return float(info['price'])
