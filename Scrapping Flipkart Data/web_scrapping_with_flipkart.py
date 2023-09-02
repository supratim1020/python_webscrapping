import pandas as pd
import requests
from bs4 import BeautifulSoup

# url = "https://www.flipkart.com/search?q=smartphone+under+50000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_2_19_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_2_19_na_na_na&as-pos=2&as-type=RECENT&suggestionId=smartphone+under+50000&requestId=423a6114-cb8a-46cf-b71a-ed5f68bf5aa8&as-backfill=on"
url=input("Enter a Flipkart url: \n")

Product_Name=[]
Prices=[]
Descriptions=[]
Reviews=[]

endpage=10
for i in range(1,endpage+1):
    temp=url
    temp=temp+"&page="+str(i)

    r = requests.get(temp)

    soup = BeautifulSoup(r.text, "lxml")
    box=soup.find("div",class_="_1YokD2 _3Mn1Gg")   # the part of the web page we want to scrap
    # print(soup)

    # scrapping name of the product
    # a list with div tag
    names=box.find_all("div",class_="_4rR01T")
    for i in names:
        Product_Name.append(i.text)
    # print(len(Product_Name))

    # scrapping prices
    prices=box.find_all("div",class_="_30jeq3 _1_WHN1")
    for i in prices:
        Prices.append(i.text)
    # print(len(Prices))

    # scrapping descriptiption
    desc=box.find_all("ul",class_="_1xgFaf")
    for i in desc:
        Descriptions.append(i.text)
    # print(len(Descriptions))

    # scrapping reviews
    reviews=box.find_all("div",class_="_3LWZlK")
    for i in reviews:
        Reviews.append(i.text)
    # print((Reviews))
    # print(len(Reviews))
    if(len(Reviews)<len(Product_Name)):
        Reviews.extend(['']*(len(Product_Name)-len(Reviews)))
    # if length of each list isn't same then we can't work with pandas and can't save to a excel

df=pd.DataFrame({"Product Name":Product_Name, "Price":Prices, "Description":Descriptions, "Review":Reviews})
print(df)
df.to_csv('scrapped_data.csv')
