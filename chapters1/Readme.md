## 第一次使用 - 連線設定

在開始交易之前，我們需要完成基本的連線設定，包括安裝相關套件、設定憑證，以及測試登入。

### 1. 安裝必要套件

本教學為 Python 的開發環境，請依據需求安裝對應的套件。

#### Python
```bash
pip install fubon_neo-<version>-cp37-abi3-win_amd64.whl
```

### 2. 憑證設定
請將您的憑證放置於資料夾內，確保結構如下：
```
.
└── XXXXXXXXXX.pfx
```

### 3. 測試連線與登入
若您未曾使用 SDK 進行過登入，或更換了 SDK 執行環境，請在資料夾內新增 `index.py` 檔案，貼上以下內容並執行：

```python
from fubon_neo.sdk import FubonSDK, Order
from fubon_neo.constant import TimeInForce, OrderType, PriceType, MarketType, BSAction

sdk = FubonSDK()
   
accounts = sdk.login("您的身分證字號", "您的登入密碼", "您的憑證位置", "您的憑證密碼") # 若有歸戶，則會回傳多筆帳號資訊
## accounts = sdk.login("您的身分證號", "您的登入密碼", "您的憑證路徑位置")  # 若憑證選用＂預設密碼＂, SDK v1.3.2與較新版本適用

acc = accounts.data[0]
```

### 4. 確認連線是否成功
執行 `index.py` 之後，若成功登入，應該會返回您的帳戶資訊。

如果出現錯誤，請確認：
- API 金鑰與憑證是否正確
- 網路環境是否允許 API 連線
- Python 環境是否安裝了必要套件
