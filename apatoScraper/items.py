# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SewaApartmentItem(scrapy.Item):
    # define the fields for your item here like:
    raw = scrapy.Field()
    area = scrapy.Field(serializer=str)
    url_item = scrapy.Field(serializer=str)
    title = scrapy.Field(serializer=str)
    description = scrapy.Field(serializer=str)
    images = scrapy.Field(serializer=str)
    contacts = scrapy.Field(serializer=str)
    posted_at = scrapy.Field(serializer=str)
