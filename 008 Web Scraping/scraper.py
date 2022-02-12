
import requests
from bs4 import BeautifulSoup


URL="https://www.amazon.com/Sperry-Womens-Sneaker-White-Medium/dp/B0116IHMI2/ref=sr_1_25?keywords=sperry%2Bshoes%2Bfor%2Bwomen&qid=1644629353&sprefix=sperr%2Caps%2C333&sr=8-25&th=1&psc=1"

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}

page=requests.get(URL,headers=headers)


soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title=soup2.find(id="productTitle").getText()
price=soup2.find(attrs="a-price a-text-price a-size-medium apexPriceToPay").get_text()
converted_price=price[0:6]

if(converted_price < 50):
    send_mail()

print(converted_price)
print(title)