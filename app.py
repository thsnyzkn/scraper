import requests
from bs4 import  BeautifulSoup
import pandas as pd

url = 'https://www.showtv.com.tr/yayin-akisi'

try:
  page_response = requests.get(url,timeout=5)

  if page_response.status_code == 200:
    page_content = BeautifulSoup(page_response.content,'html.parser')
    my_divs = page_content.find_all("div", {"class": "streaming-container clearfix"})
    for my_div in my_divs:
      my_series = my_div.find_all("div",{"class":"series"})
      for my_serie in my_series:
        my_titles = my_serie.find_all("div",{"class":"title"})
        my_clocks = my_serie.find_all("div",{"class":"clock"})
        for my_title,my_clock in zip(my_titles,my_clocks):
            print(my_title.find('span').text)
            print(my_clock.find_all('span')[0].text + " " + my_clock.find_all('span')[1].text)
  else:
    print(page_response.status_code)
except requests.Timeout as e:
  print('Timeout occurred for requested page: ' + url)
  print(str(e))