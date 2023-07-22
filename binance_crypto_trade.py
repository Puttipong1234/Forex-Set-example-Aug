import ccxt
from config import *

exchange = ccxt.binance({
        'apiKey' : BINANCE_FUTURE_API_KEY ,
        'secret' : BINANCE_FUTURE_API_SECRET ,
        'options' : {
                'defaultType' : 'future'
        }
})

exchange.set_sandbox_mode(BINANCE_FUTURE_TESTING) # True => testnet , False => mainnet   

# balance = exchange.fetch_balance(params={"type" : "future","symbols" : "USDT"})
# print(balance['info']['totalWalletBalance'])   
# position_size =  10/100 * float(balance['info']['totalWalletBalance'])
# print("position size for you is : " + str(position_size) + " USDT")

# btc_price = exchange.fetch_mark_ohlcv(symbol="BTCUSDT" , timeframe="1h")
# print(position_size/float(btc_price[-1][4]))

# OPEN LONG
# exchange.create_order(symbol="BTCUSDT",type="market",side="buy",amount=0.1)
# exchange.create_order(symbol="BTCUSDT",type="market",side="sell",amount=0.1)

# exchange.set_leverage(symbol="BTCUSDT",leverage=50)
# exchange.set_margin_mode(symbol="BTCUSDT",marginMode="isolated")

def binance_future_open_long(sym,amount):
        
        param = {"positionSide" : "LONG"}
        
        exchange.create_order(symbol=sym,
                              type="market",
                              side="buy",
                              amount=amount,
                              params=param)

def binance_future_tpsl_long(sym,amount):
        
        param = {"positionSide" : "LONG"}
        
        exchange.create_order(symbol=sym,
                              type="market",
                              side="sell",
                              amount=amount,
                              params=param)


def binance_future_open_short(sym,amount):
        
        param = {"positionSide" : "SHORT"}
        
        exchange.create_order(symbol=sym,
                              type="market",
                              side="sell",
                              amount=amount,
                              params=param)

def binance_future_tpsl_short(sym,amount):
        
        param = {"positionSide" : "SHORT"}
        
        exchange.create_order(symbol=sym,
                              type="market",
                              side="buy",
                              amount=amount,
                              params=param)


exchange_spot = ccxt.binance({
        'apiKey' : BINANCE_SPOT_API_KEY ,
        'secret' : BINANCE_SPOT_API_SECRET ,
        'options' : {
                'defaultType' : 'spot'
        }
})

exchange_spot.set_sandbox_mode(BINANCE_SPOT_TESTING)


# r = exchange_spot.create_order(symbol="XRPUSDT",type="market",side="sell",amount=10000)

# bal = exchange_spot.fetch_balance()
# assets = bal["info"]["balances"]
# for asset in assets:
#         print(asset)

def binance_buy_spot(sym,amt):
        exchange_spot.create_order(symbol=sym,
                                   type="market",
                                   side="buy",
                                   amount=amt)

        bal = exchange_spot.fetch_balance()
        assets = bal["info"]["balances"]
        for asset in assets:
                print(asset)

def binance_sell_spot(sym,amt):
        exchange_spot.create_order(symbol=sym,
                                   type="market",
                                   side="sell",
                                   amount=amt)
        bal = exchange_spot.fetch_balance()
        assets = bal["info"]["balances"]
        for asset in assets:
                print(asset)

def check_port():
        bal = exchange_spot.fetch_balance()
        assets = bal["info"]["balances"]
        for asset in assets:
                print(asset)
        return assets