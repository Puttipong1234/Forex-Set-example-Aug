import requests
r = requests.post('https://b523-2001-fb1-181-bc81-8503-4bff-ac2f-4688.ngrok-free.app/settrade/broker/spot', 
json={
        "ACTION" : "OPEN LONG" ,
        "SYMBOL" : "PTT" ,
        "AMOUNT" : 200,
        "LIMIT" : 35
})

print(r.text)