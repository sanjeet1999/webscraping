

## Project Scraper
***

Few Days back, I was given some [websites](#websites) and asked to extract some important data out of it. First it seems hectic to do this work manually. That would take a lot of effort and time. I, as a lazy person, need to find a way which could automate this task. Then web Scraping comes into picture. It has 3 program in this project
1. [Amazon Bestseller scraping](https://github.com/sanjeet1999/webscraping/tree/master/Amazon_Book_Scraping_project)
2. [Book Scraping](https://github.com/sanjeet1999/webscraping/tree/master/Book_Scraping_Project)
3. [comic downloader](https://github.com/sanjeet1999/webscraping/tree/master/comic_scraping)
## Project Motive
---
Motive of this project is to automate the extraction of essential data from webpages. And represent them in a structured format.

## Websites 
---
- [Amazon Bestsellers](https://www.amazon.in/gp/bestsellers/books/)
- [Top Books Scraper](http://books.toscrape.com/)
- [xkcd comics](https://xkcd.com/)

## Project Description
---
### <u>1. What Does this project do? :-</u>
As the name of this project suggests [Project Scraper](#project-scraper). It scraps the essential data from a given web page of a given website. This process is called web scraping.  And it not just scraps data, but also represents them in a well defined manner. For this work this project uses some predefined python modules. 

### <u>2. Modules Used in project:- </u>
- [python 3.8.8](https://www.python.org/downloads/release/python-388/)
- [bs4 4.11.1](https://pypi.org/project/beautifulsoup4/)
- [requests 2.28.1](https://pypi.org/project/requests/)
- [pandas 1.4.3](https://pypi.org/project/pandas/)

### <u>3. Project Challanges:- </u>
In this project the most challenging part is to find the particular element tag. Which actually holds our required information. Yeah, I think that is the most challenging part . And one more thing if we are talking about the challenges of this webscraping project. Then I would like to mention that. It is difficult to perform web scraping on a dynamic website. Because the data of that website is called by javascript in the background at the run time. That is the most challenging part to extract out the data from the dynamic websites.

### 4. <u>How to run this project:- </u>
First clone this repository in your virtual environment. Then make sure you full-fill all the requirements. Which are given in the requirement.txt file. By using the command  
```python
pip install -r requirement.txt
```
 Run this command in your terminal in your environment. Then pip3 will install all the required modules which must be present in your environment to run this program. Or you can download this requirement.txt modules one by one. But that will not be considered as a pythonic way. So my suggestion is to run the above command in your virtual environment terminal. Then just simply run the .py extension file in your terminal. Eg
```python 
python comic_downloader.py
``` 
> And your xkcd comic will start downloading in a file with the name xkcd in your directory.

![Inside xkcd](https://ibb.co/R4Z5TxQ)




  




