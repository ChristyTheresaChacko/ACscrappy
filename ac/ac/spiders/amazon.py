import scrapy
from..items import AcItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.in/s?k=ac&crid=G5Y494SDDMA2&sprefix=ac%2Caps%2C313&ref=nb_sb_noss_1']

    def parse(self, response):
        items = AcItem()

        name = response.css('.s-line-clamp-2::text').extract()
        price = response.css('.a-price-whole').css('::text').extract()
        discount = response.css('.a-letter-space+ span').css('::text').extract()
        image = response.css('.s-image::attr(src)').extract()
        rate = response.css('.aok-align-bottom::text').extract()

        items['name'] = name
        items['price'] = price
        items['discount'] = discount
        items['image'] = image
        items['rate'] = rate
        yield items
