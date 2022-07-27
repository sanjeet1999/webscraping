#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import bs4
import webbrowser
import os
url = "https://xkcd.com/"
os.makedirs("xkcd",exist_ok=True)
while not url.endswith("#"):
    res = requests.get(url)
    if res.status_code == requests.codes.ok:
        print("we got the comics")
        soup = bs4.BeautifulSoup(res.text,"html.parser")
        all_links = soup.select("#comic img")#from div tag, id = comic tag, then select img tag
        if all_links == []:
            print("could not find image")
            print("image url",url)
            print(all_links)   
        else:
            img_url = "https:"+all_links[0].get('src')#from img tag get src link
            print(f"Now downloading the comics from :- {img_url}")
            res1 = requests.get(img_url)
            res1.raise_for_status()
            imageFile = open(os.path.join('xkcd', os.path.basename(img_url)),'wb')
            for chunks in res1.iter_content(100000):
                imageFile.write(chunks)
            imageFile.close()
        prevous_link = soup.select("a[rel = 'prev']")[0]#from <a> tag 'rel=prev'
        url = "https://xKcd.com"+prevous_link.get('href')
        print("prev_link",url)
print("Done")
            
            

# print(soup)
# print(all_links)
# #     prevLink = soup.select('a[rel="prev"]')[0]
# #     print(prevLink.get('href'))
# #     print("------------------------------------------------") 
 


# In[ ]:




