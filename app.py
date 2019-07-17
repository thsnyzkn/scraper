import requests
from bs4 import  BeautifulSoup
import pandas as pd

def kanald_crawler(page_content):
  my_divs = page_content.find_all("ul", {"id": "weekly-programme-guide-list"})
  for my_div in my_divs:
    my_series = my_div.find_all("li")
    for my_serie in my_series:
      my_times = my_serie.find_all("div",{"class":"col-md-3 col-sm-2 col-xs-4 time"})
      my_titles = my_serie.find_all("div",{"class":"col-md-3 col-sm-4 col-xs-4 title"})
      for my_time,my_title in zip(my_times,my_titles):
        print(my_time.find('span').text)
        print(my_title.find('a').text)
def show_crawler(page_content):
  my_divs = page_content.find_all("div", {"class": "streaming-container clearfix"})
  for my_div in my_divs:
    my_series = my_div.find_all("div",{"class":"series"})
    for my_serie in my_series:
      my_titles = my_serie.find_all("div",{"class":"title"})
      my_clocks = my_serie.find_all("div",{"class":"clock"})
      for my_title,my_clock in zip(my_titles,my_clocks):
        print(my_clock.find_all('span')[0].text + " " + my_clock.find_all('span')[1].text)
        print(my_title.find('span').text)
def requester(url):
  try:
    page_response = requests.get(url,timeout=5)
    if page_response.status_code == 200:
      page_content = BeautifulSoup(page_response.content,'html.parser')
      dots= [n for n in range(len(url)) if url.find('.', n) == n]
      if(url[dots[0]+1:dots[1]]=='showtv'):
        show_crawler(page_content)
      elif(url[dots[0]+1:dots[1]]=='kanald'):
        kanald_crawler(page_content)
    else:
     print(page_response.status_code)
  except requests.Timeout as e:
    print('Timeout occurred for requested page: ' + url)
    print(str(e))

def main():
  show_url = 'https://www.showtv.com.tr/yayin-akisi'
  kanald_url = 'https://www.kanald.com.tr/yayin-akisi'
  print('****------SHOW TV------****')
  requester(show_url)
  print('****------KANAL D------****')
  requester(kanald_url)
if __name__ == '__main__':
  main()
