# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exporters import CsvItemExporter
from sqlalchemy.orm import sessionmaker

from apatoScraper.models import db_connect, create_table, SewaApartemen, JualApartemen


class ApatoscrapperDBPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        if spider.name == 'sewa-apartemen':
            item_object = SewaApartemen()
        else:
            item_object = JualApartemen()

        item_object.area = item["area"]
        item_object.url_item = item["url_item"]
        item_object.title = item["title"]
        item_object.description = item["description"]
        item_object.image_urls = item["images"]
        item_object.contacts = item["contacts"]
        item_object.posted_at = item["posted_at"]
        item_object.raw = item["raw"]

        try:
            session.add(item_object)
            session.commit()

        except Exception as e:
            print e
            session.rollback()
            raise

        finally:
            session.close()

        return item


class ApatoscrapperCSVPipeline(object):
    def __init__(self):
        self.file = None
        self.exporter = None

    def open_spider(self, spider):
        self.file = open("./apatoScraper/results/"+spider.name+".csv", 'w+b')
        self.exporter = CsvItemExporter(self.file, unicode, delimiter=";")
        self.exporter.fields_to_export = ['area', 'url_item', 'title', 'descriptions', 'images', 'contacts',
                                          'posted_at', 'raw']
        self.exporter.start_exporting()

    def close_spider(self, _):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, _):
        # item = self.create_valid_csv(item=item)
        self.exporter.export_item(item)
        return item

    @staticmethod
    def create_valid_csv(item):
        for key, value in item.items():
            is_string = (isinstance(value, basestring))
            if is_string and ("," in value.encode('utf-8')):
                item[key] = "\"" + value + "\""

        return item
