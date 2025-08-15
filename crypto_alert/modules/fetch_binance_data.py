from binance.client import Client

api_key = ""
api_secret = ""

client = Client(api_key, api_secret)

def get_all_tickers():
    """
    Отримує список усіх криптовалют з Binance з цінами.
    """

    return client.get_all_tickers()

def get_all_symbols():
    """
    Отримує список лише символів криптовалют з Binance.
    """
    tickers = get_all_tickers()
    return [ticker['symbol'] for ticker in tickers]