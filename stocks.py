import yfinance as yf
from tabulate import tabulate


tickers = [
    'SPY',
    'VOO',
    'MSFT',
]


def run():
    stocks = []

    for ticker in tickers:
        data = get_data(ticker)
        current_price = format_price(data['current_price'])
        movement = format_change(data['movement'])
        stocks.append([ticker, current_price, movement])

    print(tabulate(stocks))


def format_change(change):
    return f'{round(change, 2)} %'


def format_price(price):
    return f'$ {round(price, 2)}'


def get_data(ticker):
    ticker_result = yf.Ticker(ticker)
    history = ticker_result.history()

    current_price = history.tail(1)['Close'].iloc[0]
    prev_close = history.tail(2)['Close'].iloc[0]

    movement = ((current_price - prev_close) / prev_close) * 100
    return {
        'current_price': current_price,
        'movement': movement
    }


if __name__ == '__main__':
    run()
