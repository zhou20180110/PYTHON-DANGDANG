import scrapy
from bs4 import BeautifulSoup
from ..items import DangdangItem
class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['bang.dangdang.com']
    start_urls = []
    for i in range(1,4):
        start_urls.append('http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-'+str(i))
    def parse(self,response):
        soup = BeautifulSoup(response.text,'html.parser')
        li = soup.find(class_='bang_list clearfix bang_list_mode').find_all('li')
        for i in li:
            title = i.find(class_='name').find('a')['title']
            zuozhe = i.find(class_='publisher_info').find('a')['title']
            price = i.find(class_='price_n').text
            it = DangdangItem()
            it['name']=title
            it['zuozhe']=zuozhe
            it['price']=price
            print(title)
            yield it
