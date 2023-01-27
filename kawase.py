import pandas as pd
from datetime import datetime
from forex_python.converter import CurrencyRates

"""
********************************
引数情報（要チェック）
********************************
"""
# 開始日
start_date = datetime(2023, 1, 2, 0, 0)
# 終了日
end_date   = datetime.today()

# 通貨ペア｜基準通貨
currency_1 = 'USD'
# 通貨ペア｜比較通貨
currency_2 = 'JPY'


"""
********************************
実行（以下修正不要）
********************************
"""
# FX Object
obj = CurrencyRates()

# 為替レート計算
def historical_rate(datetime,currency1, currency2):
    try:
        return obj.get_rate(currency1, currency2, datetime)
    
    except Exception as re:
        print(re)
        return None

# データフレーム
df = pd.DataFrame(pd.date_range(start = start_date,  # 開始日
                                end   = end_date,    # 終日
                                freq  = 'B'          # 営業日のデータのみ取得(Only Business Day)
                                ), 
                  columns=['DateTime']
                 )

# 結果加工
currency_pair      = currency_1 + "/" + currency_2
df[currency_pair]  = df['DateTime'].apply(historical_rate, args=(currency_1,currency_2))

# 出力
print(df)