# coding=utf-8
from apatoScraper.spiders.apartemen import ApartemenSpider


class SewaApartemenSpider(ApartemenSpider):
    name = 'sewa-apartemen'
    start_urls = [
        'https://www.sewa-apartemen.net/',
    ]

    custom_settings = {'FEED_URI': "./apatoScraper/results/" + name + "_%(time)s.json",
                       'FEED_FORMAT': 'json'}  # json or csv format
