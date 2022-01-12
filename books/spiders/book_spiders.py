import scrapy
from books.items import BooksItem


class BookSpider(scrapy.Spider):
    name = "books"
    page_number = 1
    start_urls = ['http://www.quanshuwang.com/list/5_1.html']

    def parse(self, response):
        books = response.selector.xpath('//*[@id="navList"]/section/ul/li/span/a[1]//@href').getall()
        for book in books:
            yield scrapy.Request(book, callback=self.parse_book)

        next_page = response.selector.xpath('//*[@id="pagelink"]/a[12]/@href').get()
        if next_page is not None:
            yield scrapy.Request(next_page)

    def parse_book(self,response):
        items = BooksItem()
        items['book_name'] = response.selector.css("h1::text").extract()[0]
        items['author_name'] = response.selector.xpath('//*[@id="container"]/div[2]/section/div/div[4]/div[1]/dl[2]/dd/text()').extract()[0]
        items['book_introduction'] = "\n".join(response.selector.xpath('//*[@id="waa"]/text()').extract())
        items['lu_chapter_names'] = response.selector.xpath('//*[@id="container"]/div[2]/section/div/div[4]/div[1]/dl[3]/dd/ul/li[1]/a/text()').extract()[0]
        items['lu_chapter_update_time'] = response.selector.xpath('//*[@id="container"]/div[2]/section/div/div[4]/div[1]/dl[3]/dd/ul/li[1]/text()').extract()[0]
        yield items
