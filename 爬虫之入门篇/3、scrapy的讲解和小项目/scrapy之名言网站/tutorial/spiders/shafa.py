# -*- coding: utf-8 -*-
import scrapy


class ShafaSpider(scrapy.Spider):
    name = 'shafa'
    allowed_domains = ['gz.58.com']
    start_urls = ["https://gz.58.com/jiajushafa/pn2/",
                    "https://gz.58.com/jiajushafa/pn3/"]

    def parse(self, response):
        pn = response.url.split("/")[-2]
        filename ="shafa-{}.html".format(pn)
        with open(filename,"w") as f:
            shafas = response.css(".tdiv")
            for shafa in shafas:
                title = shafa.css(".item-desc::text").extract()
                dizhi = shafa.css(".seller::text").extract()
                jiage = shafa.css(".pri::text").extract()
                print("dizhi:\n",dizhi)
                print("title:\n",title)
                print("jiage:\n",jiage)
                f.write("title:{}\n dizhi:{}\n jiage:{}\n".format(title,dizhi,jiage))