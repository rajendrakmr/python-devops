import requests


def api_call_data(api):

    response = requests.get(url=api)
    for key,value in response.json().items():
        if key == "Meta Data":
            return value
    return response.json()


API_KEY = "demo"
SYMBOL = input('Enter the symbol for Stock Market eg. AMZN, IBM,')
INTERVAL = "1min"
API_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&interval={INTERVAL}&apikey={API_KEY}"




data = api_call_data(API_URL)



print(data)

