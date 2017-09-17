import requests
from bs4 import BeautifulSoup
def trade_spider(max_pages):
    page = 1
    while page <=max_pages:
        url='http://www.m4maths.com/frequently-asked-placement-questions.php?ISSOLVED=&page='+str(page)+'&LPP=10&SOURCE=3i-Infotech&MYPUZZLE=&UID=&TOPIC=&SUB_TOPIC='
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        for link in soup.find_all('h2',({id: 'quotes'})):
            href = link.get('href')
            title=link.h2
            print(href)
            print(title)

        page += 1

trade_spider(181)
