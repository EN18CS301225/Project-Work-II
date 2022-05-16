
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import render
from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib.request
import time
import random

def reading(request):
     return render(request,"affirmation_reading/affirmation_reading.html")

# Create your views here.
def get_html_content():
    import requests
    
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE


#image scrapping





#Create lists to store the scraped data
authors = []
quotes = []    

def scrape_website(page_number):
   
    page_num = str(page_number) #Convert the page number to a string
    URL = 'https://www.goodreads.com/quotes/tag/inspirational?page='+page_num #append the page number to complete the URL
    webpage = requests.get(URL)  #Make a request to the website
    soup = BeautifulSoup(webpage.text, "html.parser") #Parse the text from the website
    quoteText = soup.find_all('div', attrs={'class':'quoteText'}) #Get the tag and it's class
    for i in quoteText:
        quote = i.text.strip().split('\n')[0]#Get the text of the current quote, but only the sentence before a new line
        author = i.find('span', attrs={'class':'authorOrTitle'}).text.strip()
        #print(quote)
        quotes.append(quote)
        #print(author)
        authors.append(author)



def home(request):
    #Loop through 'n' pages
    n = 10
    for num in range(0,n):
        scrape_website(num)
    
    #Combine the lists
    combined_list = []
    for i in range(len(quotes)):
        combined_list.append(quotes[i]+'-'+authors[i])
        
    random_quote = random.choice(combined_list)
    
    return render(request,'affirmation_reading/home.html', {'quote': random_quote})