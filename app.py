from flask import Flask , request
import json

from binance_crypto_trade import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>This route is for Bot Trade Signals</p>"

@app.route("/crypto/binance/future",methods=["GET","POST"])
def crypto_binance_future():
    
    if request.method == "POST":
        signal = request.data.decode("utf-8")
        signal = json.loads(signal)
        print(signal)
        
        trade_side = signal["ACTION"]
        trade_symbol = signal["SYMBOL"]
        trade_amt = signal["AMOUNT"]
        
        # สร้าง order ไปที่ Exchange , broker 
        
        if "OPEN LONG" in trade_side:
                binance_future_open_long(trade_symbol,trade_amt)
        
        elif "OPEN SHORT" in trade_side:
                binance_future_open_short(trade_symbol,trade_amt)
        
        elif "TPSL LONG" in trade_side:
                binance_future_tpsl_long(trade_symbol,trade_amt)
        
        elif "TPSL SHORT" in trade_side:
                binance_future_tpsl_short(trade_symbol,trade_amt)
        
        return "200"
    
    elif request.method == "GET":
        return "This is route for /crypto/binance/future Please POST data"

if __name__ == '__main__':
    app.run(debug=True)