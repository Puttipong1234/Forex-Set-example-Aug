import requests
r = requests.post('http://127.0.0.1:5000/crypto/binance/future', 
json={
        "ACTION" : "OPEN LONG" ,
        "SYMBOL" : "LTCUSDT" ,
        "AMOUNT" : 100
})

print(r.text)