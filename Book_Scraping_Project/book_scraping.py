#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4
import requests
import pandas as pd
res = requests.get("http://books.toscrape.com/")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
data = soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
my_data = {
    "Book Name": [],
    "Rating": [],
    "price": [],
}
for i in data:
    Book_title = i.find("h3")#Book Name
    if Book_title:
        my_data["Book Name"].append(Book_title.a["title"])
#         print("Get data")
    else:
        my_data["Book Name"].append("")
    Book_Rating = i.find("p")#Book Rating
    if Book_Rating:
        Book_Rating = str(Book_Rating["class"])
        Book_Rating = Book_Rating.replace("[","").replace("]","")
        Book_Rating = Book_Rating.replace(",","").replace("' '"," ")
        Book_Rating = Book_Rating.replace("'","").replace("'","")
        my_data["Rating"].append(Book_Rating)
    else:
        my_data["Rating".append("")]
    Book_price = i.find("div",class_="product_price")# Book Price
    if Book_price:
        if Book_price.find("p",class_="price_color"):
            if Book_price.find("p",class_="price_color").text:
                my_data["price"].append(Book_price.find("p",class_="price_color").text)
    else:
        print("No data")
Data_frame = pd.DataFrame(my_data)
Data_frame


# In[2]:


Data_frame.to_csv("book_details.csv")


# In[ ]:




