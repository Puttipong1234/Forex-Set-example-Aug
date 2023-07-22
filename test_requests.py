import requests
r = requests.post('http://127.0.0.1:5000/crypto/binance/spot', 
json={
        "ACTION" : "OPEN LONG" ,
        "SYMBOL" : "LTCUSDT" ,
        "AMOUNT" : 10
})

print(r.text)