from settrade_v2 import Investor
from config import *


investor = Investor(
                app_id="podzKYoZPAcfv6Ov",                                 
                app_secret="AP0SQNpqgIobNh2l23jGPYaHs/16PzDtR0Mc/2rkGHle", 
                broker_id="SANDBOX",
                app_code="SANDBOX",
                is_auto_queue = False)

deri = investor.Derivatives(account_no=SETTRADE_FUTURE_ACC_NO) 

print(deri.get_account_info())