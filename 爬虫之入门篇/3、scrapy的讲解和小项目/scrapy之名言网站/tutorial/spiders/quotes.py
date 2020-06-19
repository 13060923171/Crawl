# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/',
                    'http://quotes.toscrape.com/page/2/']

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = "quotes - {}.txt".format(page)
        with open(filename,"w") as f:
            quotes = response.css(".quotes")
            for quote in quotes:
                title = quote.css(".text::text").extract()[0]
                author = quote.css(".author::text").extract()[0]
                print("title:\n",title)
                print("author:\n",author)
                tags = quote.css(".tag::text").extract()
                print("tags:\n",tags)
                f.write("title:\n{}\n author:{}\n tags:{}\n".format(title,author,tags))

