from csv import excel
import pandas as pd

excel_file='BTC_USD_2014-11-04_2022-01-26-CoinDesk.csv'

df=pd.read_csv(excel_file)
# print(df.columns)
# print(df.head(5))

new_df=df.loc[:,"Date":"Closing Price (USD)"]
# print(new_df)

simple_moving_average= new_df.rolling(window=7, on='Date').mean()
print(simple_moving_average)