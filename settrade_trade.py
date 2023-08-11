from settrade_v2 import Investor
from config import *


investor = Investor(
                app_id=SETTRADE_APP_KEY,                                 
                app_secret=SETTRADE_APP_SECRET, 
                broker_id=SETTRADE_TESTING,
                app_code=SETTRADE_TESTING,
                is_auto_queue = False)

future = investor.Derivatives(account_no=SETTRADE_FUTURE_ACC_NO)
spot = investor.Equity(account_no=SETTRADE_SPOT_ACC_NO)


def SETTRADE_SPOT_BUY(sym,amt):
        print("Buying here")
        spot.place_order(
                pin=SETTRADE_PINCODE,
                side="Buy",
                symbol=sym,
                volume=int(amt),
                price_type = "MP-MTL",
                price=0,
        )

def SETTRADE_SPOT_SELL(sym,amt):
        print(amt)
        spot.place_order(
                pin=SETTRADE_PINCODE,
                side="Sell",
                symbol=sym,
                volume=int(amt),
                price_type = "MP-MTL",
                price=0,
        )

# 4 function future (long short , tpsl , open)
if __name__ == '__main__':
        # print(future)
        # print(spot.get_account_info())
        
        # spot.place_order(
        #         pin=SETTRADE_PINCODE,
        #         side="Sell",
        #         symbol="PTT",
        #         volume=1000,
        #         price_type = "MP-MTL",
        #         price=0,
        # )
        
        mkt_data = investor.MarketData()
        # res = mkt_data.get_quote_symbol("PTT")
        
        print(mkt_data.get_quote_symbol())