import plotly
import plotly.graph_objects as go
import pandas as pd


excel_file='Office_Supplies_Sales.xlsx'
df=pd.read_excel(excel_file)
# print(df)

data = [go.Scatter(x=df['OrderDate'], y=df['Total'])]
fig=go.Figure(data)
# fig.show()

plotly.offline.plot(fig, filename='Office_Supplies_Sales.html')