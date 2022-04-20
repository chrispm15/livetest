import ccxt

exchange = 'kucoin'         # change this variable to select which exchange you wish to use

if exchange == 'coinbase':
    exchange = ccxt.coinbase()
elif exchange == 'coinbasepro':
    exchange = ccxt.coinbasepro()
elif exchange == 'binance':
    exchange = ccxt.binance()
elif exchange == 'binanceus':
    exchange = ccxt.binanceus()
elif exchange == 'kucoin':
    exchange = ccxt.kucoin()
else:
    print("Exchange not handled by script.\n\n"
          "List of handled exchanges:\n-coinbase\n-coinbasepro\n-binance\n-binanceus\n-kucoin\n\n"
          "List of supported exchanges (note: you will need to add the following line 'exchange = ccxt.{exchange}':")
    print(ccxt.exchanges)


class Fees:                 # handles trading fees. could add slippage variable if you wish to estimate it.
    maker = .005
    taker = .01

class Long:                 # handles the opening and closing of long trades

    def open(ticker):
        openFill = exchange.fetch_ticker(ticker)['ask']
        return openFill

    def close(ticker):
        closeFill = exchange.fetch_ticker(ticker)['bid']
        return closeFill

class Short:                #handles the opening and closing of short trades

    def open(ticker):
        openFill = exchange.fetch_ticker(ticker)['bid']
        return openFill

    def close(ticker):
        closeFill = exchange.fetch_ticker(ticker)['ask']
        return closeFill

class Ret:                  # handles calculating a trade's return

    def longRet(open, close):
        r = (close - open) / open
        r = round(r, ndigits=4)
        return r
    def shortRet(open, close):
        r = (open - close) / open
        r = round(r, ndigits=4)
        return r
