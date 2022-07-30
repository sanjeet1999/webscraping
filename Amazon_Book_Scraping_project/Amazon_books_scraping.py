#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import bs4
import requests
res = requests.get("https://www.amazon.in/gp/bestsellers/books/")
print(res)
soup = bs4.BeautifulSoup(res.text,"html.parser")
all_books_name = soup.find_all("div",{"id" : "gridItemRoot"})
j = 0
my_books = {
    'book name' : [],
    'Author name' : [],
    "Ratings" : []
}
for i in all_books_name:
    j+=1
    book_content = i.find("div",class_="zg-grid-general-faceout")
    author_name = i.find("div",class_="a-row a-size-small")
    ratings = i.find("div",class_="a-icon-row")

    if book_content:
        if book_content.find('span'):
            my_books['book name'].append(book_content.find('span').text) 
        else:
            my_books['book name'].append("") 
    else:
        my_books['book name'].append("") 

        
    if author_name:
        if author_name.find('div'):
            my_books['Author name'].append(author_name.find('div').text)
        else:
            my_books['Author name'].append("")
    else:
        my_books['Author name'].append("")

        
    if ratings:  
        if ratings.find('a'):
            my_books['Ratings'].append(ratings.find('a')["title"])
        else:
            my_books['Ratings'].append(ratings.a[""])
    else:
        my_books['Ratings'].append("")


# In[3]:


print(my_books)


# In[4]:


dataframe = pd.DataFrame(my_books)
dataframe.head()
# dataframe.to_csv('amazon_books.csv')


# In[ ]:




