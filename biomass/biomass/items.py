# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BiomassItem(scrapy.Item):
    # define the fields for your item here like:
    week = scrapy.Field()
    url = scrapy.Field()
    articles = scrapy.Field()

