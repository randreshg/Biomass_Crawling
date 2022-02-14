import scrapy
from ..items import BiomassItem

class WeekSpider(scrapy.Spider):
    name = "weeks"
    start_urls = [
        'http://biomassmagazine.com/newsletter/biomass-week/'
    ]

    def parse(self, response):
        elements = response.css('#colLeft a')
        for i in range(0, 10):
            element = elements[i]
        #for element in elements:
            week = element.css('::text').extract_first()
            url = element.css('::attr(href)').extract_first()
            # Items
            if week and url:
                yield response.follow(url, callback=self.parseWeek, meta={'week':week, 'url':url})

    def parseWeek(self, response):
        # Item
        item = BiomassItem()
        item['week'] = response.meta['week']
        item['url'] = response.meta['url']
        # Articles
        articles = []
        elements = response.css('#articles div')
        for element in elements:
            article = {}
            article['title'] = element.css('h3::text').extract_first()
            article['description'] = element.css('span::text').extract_first()
            article['url'] = element.css('br+ a::attr(href)').extract_first()
            articles.append(article)
            item['articles'] = articles
        yield item