import requests
from lxml import etree

url='http://movie.bcoiu.cn/'
res=requests.get(url).text
html=etree.HTML(res)
a=html.xpath('//ul[@class="top-nav"]')[0]
for i in a:
    type=a.xpath('.//text()')
    print(type)