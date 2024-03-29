# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    book_name = scrapy.Field()
    author_name = scrapy.Field()
    book_introduction = scrapy.Field()
    lu_chapter_names = scrapy.Field()
    lu_chapter_update_time = scrapy.Field()
    pass
