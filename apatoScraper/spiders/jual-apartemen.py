# coding=utf-8
from apatoScraper.spiders.apartemen import ApartemenSpider


class JualApartemenSpider(ApartemenSpider):
    name = 'jual-apartemen'
    start_urls = [
        'https://www.jual-apartemen.com/',
    ]

    custom_settings = {'FEED_URI': "./apatoScraper/results/" + name + "_%(time)s.json",
                       'FEED_FORMAT': 'json'}
