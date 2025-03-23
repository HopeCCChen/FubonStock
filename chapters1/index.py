# 匯入 SDK Library
from fubon_neo.sdk import FubonSDK, Order
from fubon_neo.constant import TimeInForce, OrderType, PriceType, MarketType, BSAction
from config import ACCOUNT, PASSWORD, CERT_PATH, CERT_PASSWORD

sdk = FubonSDK()
print(ACCOUNT,CERT_PATH)
accounts = sdk.login(ACCOUNT, PASSWORD, CERT_PATH)   # 登入帳號
#accounts = sdk.login(ACCOUNT, PASSWORD, CERT_PATH,CERT_PASSWORD)   # 登入帳號

print(accounts)
sdk.init_realtime() # 建立行情元件連線

print(accounts)

inventories = sdk.accounting.inventories(accounts.data[0])
print(inventories)