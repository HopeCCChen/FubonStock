
### Python
```bash
pip install fubon_neo-<version>-cp37-abi3-win_amd64.whl
```

### 憑證設定
請將您的憑證放置於資料夾內，資料夾結構應如下所示：
```
.
└── XXXXXXXXXX.pfx
```

### 登入與測試
若您未曾使用 SDK 進行過登入，或更換了 SDK 執行環境，請在資料夾內新增一個 `index.py` 檔案，貼上以下內容並執行：

```python
from fubon_neo.sdk import FubonSDK, Order
from fubon_neo.constant import TimeInForce, OrderType, PriceType, MarketType, BSAction

sdk = FubonSDK()
   
accounts = sdk.login("您的身分證字號", "您的登入密碼", "您的憑證位置", "您的憑證密碼") # 若有歸戶，則會回傳多筆帳號資訊
## accounts = sdk.login("您的身分證號", "您的登入密碼", "您的憑證路徑位置")  # 若憑證選用＂預設密碼＂, SDK v1.3.2與較新版本適用

acc = accounts.data[0]
```