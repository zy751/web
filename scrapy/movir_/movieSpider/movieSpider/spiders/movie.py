import scrapy
import re
from ..settings import STR
class MovieSpider(scrapy.Spider):
    name='movie'
    allowed_domains=['movie.bcoiu.cn']
    start_urls=['http://movie.bcoiu.cn']
    def parse(self, response):
            yield scrapy.Request(
                f'http://movie.bcoiu.cn/?m=vod-type-id-{STR}.html',
                callback=self.parse_next,
            )

    def parse_movie(self,response):
        info_list=response.xpath('//div[@class="main"]/div[3]//li')
        for i in info_list:
            title=i.xpath('./a/@title').getall()[0]
            href='http://movie.bcoiu.cn'+i.xpath('./a/@href').getall()[0]
            imghref=i.xpath('./a/img/@data-original').getall()[0]
            yield scrapy.Request(
                href,
                callback=self.getdetail,
                meta={'url':href}
            )

    def parse_next(self,response):
        number=response.xpath("//div[contains(@class,'page')]/text()[1]").getall()[0]
        res=re.findall('/(.*)页',number)[0]
        if(int(res)>10):
            res=10
        else:
            res=int(res)
        for i in range(1,res+1):
            yield scrapy.Request(
                f'http://movie.bcoiu.cn/?m=vod-type-id-{STR}-pg-{i}.html',
                callback=self.parse_movie,
            )

    def getdetail(self,response):
        url=response.meta['url']
        infolist=response.xpath('//div[@class="ct-c"]')
        imgsrc=response.xpath('//div[@class="ct-l"]/img/@data-original').getall()[0]
        for info in infolist:
            title = info.xpath('.//dt[1]/text()').getall()[0]
            try:
                if(len(info.xpath('.//dt[2]//a/text()').getall())>3):
                    pers = ','.join(info.xpath('.//dt[2]//a/text()').getall()[:3])
                else:
                    pers=','.join(info.xpath('.//dt[2]//a/text()').getall())
            except:
                pers=''
            type=info.xpath('.//dt[3]/a/text()').getall()[0]
            infos=''.join(info.xpath('//div[@class="ct-c"]//dd//text()').getall()).replace('\xa0','')
            author=re.findall('导演：(.*)地区',infos)[0].strip()
            area=re.findall('地区：(.*)年份',infos)[0].strip()
            year=re.findall('年份：(.*)语言',infos)[0].strip()
            mes=info.xpath('./div[@name="ee"]/text()').getall()[0].replace(u'\u3000',u'').replace('\n','').replace(u'\xa0',u'').replace('本片由贝壳影视提供在线播放,如果您喜欢请把本站分享给您的朋友谢谢支持!','').strip()
            item={
                'title':title,
                'href':url,
                'imgsrc':imgsrc,
                'pers':pers,
                'type':type,
                'author':author,
                'area':area,
                'year':year,
                'mes':mes,
            }
            print(item)
            yield item