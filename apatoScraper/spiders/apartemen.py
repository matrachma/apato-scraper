# coding=utf-8
import scrapy
import unicodedata

from apatoScraper.items import SewaApartmentItem


class ApartemenSpider(scrapy.Spider):
    name = ''
    start_urls = []

    def parse(self, response, **kwargs):
        for area in response.xpath('//li[contains(@class,"cat-item-16")]/ul/li/a/@href').getall():
            yield scrapy.Request(area, callback=self.parse_area)

    def parse_area(self, response):
        listing = response.xpath('//div[contains(@class, "status-publish")]')
        for i, l in enumerate(listing):
            yield self.parse_item(l, response.url)

        paging = response.xpath('//div[@id="wp_page_numbers"]/ul/li')
        next_page_url = None
        for index, p in enumerate(paging):
            if p.xpath('a/text()').get() == u'>':
                next_page_url = p.xpath('a/@href').get()
                print(next_page_url)

        if next_page_url is not None:
            yield scrapy.Request(next_page_url, callback=self.parse_area)

    @staticmethod
    def parse_item(selected, url):
        raw = selected.get()
        url_split = url.split('/')
        if 'page' in url_split:
            area = url_split[-4]
        else:
            area = url_split[-2]
        url_item = selected.xpath('div[@class="post-headline"]/h2/a/@href').get()
        title = unicodedata.normalize(
            'NFKD', selected.xpath('div[@class="post-headline"]/h2/a/text()').get()).encode('ascii', 'ignore')
        body = selected.xpath('div[@class="post-bodycopy clearfix"]')
        images = ' '.join(map(str, body.xpath('p/a/@href').getall()))
        descriptions = []
        contacts = []
        for i, li in enumerate(body.xpath('ul/li')):
            li_text = ""
            try:
                if li.xpath('text()').get() is not None:
                    li_text = unicodedata.normalize(
                        'NFKD', li.xpath('text()').get()
                    ).encode('ascii', 'ignore').rstrip("\n")
                elif li.xpath('strong/text()').get() is not None:
                    li_text = unicodedata.normalize(
                        'NFKD', li.xpath('strong/text()').get()
                    ).encode('ascii', 'ignore').rstrip("\n")
                if li.xpath('strong/text()').get() is not None:
                    li_text += unicodedata.normalize(
                        'NFKD', li.xpath('strong/text()').get()
                    ).encode('ascii', 'ignore').rstrip("\n")
                elif li.xpath('a/text()').get() is not None:
                    li_text += unicodedata.normalize(
                        'NFKD', li.xpath('a/text()').get()
                    ).encode('ascii', 'ignore').rstrip("\n")
                descriptions.append(li_text)
            except Exception as e:
                print e
                print li
                print url_item

            li_ul = li.xpath('ul/li')
            if len(li_ul) > 0:
                for _, li_ul_li in enumerate(li_ul):
                    try:
                        li_ul_li_text = '\t' + unicodedata.normalize(
                            'NFKD', li_ul_li.xpath('//text()').get()).encode('ascii', 'ignore')
                        descriptions.append(li_ul_li_text)
                    except Exception as e:
                        print e
                        print li_ul_li
                        print url_item

            lower_li_text = li_text.lower()
            if "contact" in lower_li_text or "mail" in lower_li_text or "whatsapp" in lower_li_text:
                contacts.append(li_text)
        posted_at = selected.xpath('div[@class="post-footer"]/text()').get().split(" | ")[0]

        description = "\n".join(descriptions)
        contact = "\n".join(contacts)
        apato_item = SewaApartmentItem(
            raw=raw, area=area, url_item=url_item, title=title, description=description,
            images=images, contacts=contact, posted_at=posted_at
        )
        return apato_item
        # print(area, url_item, title, images, description)
