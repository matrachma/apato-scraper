from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Text
from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


class SewaApartemen(Base):
    __tablename__ = "sewa_apartemen"

    id = Column(Integer, primary_key=True)
    area = Column('area', Text())
    url_item = Column('url_item', Text())
    title = Column('title', Text())
    description = Column('description', Text())
    image_urls = Column('image_urls', Text())
    contacts = Column('contacts', Text())
    posted_at = Column('posted_at', Text())
    raw = Column('raw', Text())


class JualApartemen(Base):
    __tablename__ = "jual_apartemen"

    id = Column(Integer, primary_key=True)
    area = Column('area', Text())
    url_item = Column('url_item', Text())
    title = Column('title', Text())
    description = Column('description', Text())
    image_urls = Column('image_urls', Text())
    contacts = Column('contacts', Text())
    posted_at = Column('posted_at', Text())
    raw = Column('raw', Text())
