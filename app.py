from flask import Flask , request
import json

from binance_crypto_trade import *
from settrade_trade import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>This route is for Bot Trade Signals</p>"

@app.route("/crypto/binance/spot",methods=["GET","POST"])
def crypto_binance_spot():
    
    if request.method == "POST":
        signal = request.data.decode("utf-8")
        signal = json.loads(signal)
        print(signal)
        
        trade_side = signal["ACTION"]
        trade_symbol = signal["SYMBOL"]
        trade_amt = signal["AMOUNT"]
        
        # สร้าง order ไปที่ Exchange , broker 
        
        if "OPEN LONG" in trade_side:
                binance_buy_spot(trade_symbol,trade_amt)
        
        elif "TPSL LONG" in trade_side:
                partial = float(trade_side.split(" ")[-1])
                binance_sell_spot(trade_symbol,trade_amt*partial/100)
        
        return "200"
    
    elif request.method == "GET":
        return check_port()

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
                partial = float(trade_side.split(" ")[-1])
                binance_future_tpsl_long(trade_symbol,trade_amt*partial/100)
        
        elif "TPSL SHORT" in trade_side:
                partial = float(trade_side.split(" ")[-1])
                binance_future_tpsl_short(trade_symbol,trade_amt*partial/100)
        
        return "200"
    
    elif request.method == "GET":
        return "This is route for /crypto/binance/future Please POST data"

@app.route("/settrade/broker/spot",methods=["GET","POST"])
def settrade_broker_spot():
    
    if request.method == "POST":
        signal = request.data.decode("utf-8")
        signal = json.loads(signal)
        print(signal)
        
        trade_side = signal["ACTION"]
        trade_symbol = signal["SYMBOL"]
        trade_amt = signal["AMOUNT"]
        
        # สร้าง order ไปที่ Exchange , broker 
        
        if "OPEN LONG" in trade_side:
                SETTRADE_SPOT_BUY(trade_symbol,trade_amt)
        
        elif "TPSL LONG" in trade_side:
                partial = float(trade_side.split(" ")[-1])
                SETTRADE_SPOT_SELL(trade_symbol,trade_amt*partial/100)
        
        return "200"
    
    elif request.method == "GET":
        return "This is Route for SETTRADE post DATA"

from forex_trade import *

@app.route('/forex/broker/future', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        
        mt5.initialize()
        
        print("Signal from tradingview")
        print("Preparing for an order")
        print("Data incoming : " + str(request.data))
        
        # รับ Data แปลงให้เป็น dictionary
        signal = request.data.decode("utf-8")
        signal = json.loads(signal)
        
        # แยกแยะแล้วจัดเก็บใส่ตัวแปร
        symbol = signal["SYMBOL"]
        lot = float(signal["AMOUNT"])
        action = signal["ACTION"].split(" ")[0]
        side = signal["ACTION"].split(" ")[1]
        
        partial = 100
        if action == "TPSL":
            partial = int(signal["ACTION"].split(" ")[2])
        
        
        # ทำการเปิด orders + ป้องกันการเกิด requote
        while True:
            r = ""
            if action == "OPEN":
                if side == "LONG":
                    r = orders(symbol, lot)
                elif side == "SHORT":
                    r = orders(symbol, lot,buy=False)
            
            elif action == "TPSL":
                if side == "LONG":
                    r = close_orders(symbol,True ,lot*(partial/100))
                elif side == "SHORT":
                    r = close_orders(symbol,False ,lot*(partial/100))
                    
        # + ป้องกันการเกิด requote
            if r == "Requote":
                time.sleep(0.5)
                continue
            else:
                break
        
        mt5.shutdown()
        
        return request.data , 200
    else:
        return "This is a FOREX service"

if __name__ == '__main__':
    app.run(debug=True)