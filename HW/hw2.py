# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:20:48 2022

@author: Tita
"""

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


def scrap_page(page_number):#function that scrap the website
    base_web_address = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=01-20-2021&to%5Bdate%5D=08-01-2022&person2=200320&category2%5B%5D=8&items_per_page=100"
    if page_number > 0:
        #the Biden speeches have 7 pages
        web_address = base_web_address + "&page=" + str(page_number) 
    else:
        web_address = base_web_address

    # Open a web page
    web_page = urllib.request.urlopen(web_address)
    web_page #stored on machine
    
    # Parse it
    soup = BeautifulSoup(web_page.read())
    
    #Dates
    dates = soup.find_all("td", {"class": "views-field views-field-field-docs-start-date-time-value text-nowrap"})
    #Title
    titles = soup.find_all("td", {"class": "views-field views-field-title"})
    #empty lists to store text
    list_titles = []
    list_dates = []
    list_links = []
    speeches = []
    #for loop to extract the titles and lists. Append to the empty lists
    for t,d in zip(titles,dates):
        title = t.get_text()
        list_titles.append(title)
        
        date = d.get_text()
        list_dates.append(date)
        
        # Getting the link of the article
        link = "https://www.presidency.ucsb.edu" + t.find('a')['href']
        list_links.append(link)
        
        interior = link# go to interior page
        interior_speech = urllib.request.urlopen(interior) # open interior
        interior_soup = BeautifulSoup(interior_speech.read()) # soup interior
        speech = interior_soup.find("div", {"class": "field-docs-content"}) #find the text with the tags
        speeches.append(speech.get_text())#append the text to the empty list
        
    return list_titles, list_dates, list_links, speeches

#Empty lists to store the final lists
list_titles_ = []
list_dates_ = []
list_links_ = []
speeches_ = []

#for loop that use the function scrape_page and paste the lists together
for i in range(0,7):
    t,d,l,s = scrap_page(i)
    list_titles_ = list_titles_ + t
    list_dates_ = list_dates_ + d
    list_links_ = list_links_ + l
    speeches_ = speeches_ + s

#dataframe that contains the speeches, titles, dates and link
df = pd.DataFrame({"titles": list_titles_ , "date": list_dates_, "links": list_links_, "speech": speeches_})

#clean with pandas the text
df['date'] = df['date'].replace(r'\s+|\\n', ' ', regex=True)
df['speech'] = df['speech'].replace(r'\s+|\\n', ' ', regex=True)
df['speech'] = df['speech'].str.replace('"',"")
df['speech'] = df['speech'].str.replace('."',"")
df['date'] = df['date'].str.strip()
df['speech'] = df['speech'].str.strip()
df['titles'] = df['titles'].str.strip()
for speech in df:
    df['speech'] = df['speech'].str.replace('\s\d+:\d+:\d+[^a-c6]\d+$', '', regex=True)

#save as csv
df.to_csv("biden_speech.csv")


