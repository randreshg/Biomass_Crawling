import scrapy


class BiomassSpider(scrapy.Spider):
    name = "Biomass Magazine"
    start_urls = [
        'http://biomassmagazine.com/newsletter/biomass-week/'
    ]
