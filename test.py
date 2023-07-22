# basic 
# variable ตัวแปร integer (int) float string list dictionary

a = 1 
b = 0.1
c = "this is string"
d = [1,2,3,4,5,6]
d_2 = ["BTCUSD","ETHUSD","BNBUSD","EURUSD"]
symbols = ["BTCUSD","ETHUSD","BNBUSD","EURUSD"]
for x in symbols:
  print(x) 
#loop

sample_dict = {"dog" : "สุนัข" , "cat" : "แมว" , "bird" : "นก"} 
print(sample_dict["dog"])

# คำนวนจำนวน contract BTC ที่ต้องการซื้อ 
# มีเงิน 100,000 บาท
# btc ราคา คอนแทรกละ 900,000 บาท
มีเงิน = float(input("กรุณาใส่จำนวนเงิน : "))
leverage = float(input("กรุณาใส่ leverage : ")) # 2x 5x 10x
btc_price = 900000
จำนวนที่ซื้อได้ = (มีเงิน/btc_price) * leverage
print("จำนวนที่ซื้อได้ : " + str(จำนวนที่ซื้อได้) + " BTC contract")