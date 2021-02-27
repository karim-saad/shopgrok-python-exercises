import scrapy


class GrocerySpider(scrapy.Spider):
    name = 'grocery_products'

    start_urls = ['https://www.aldi.com.au/']
    
    def parse(self, response):
        for grocery_page in response.xpath('//body//div[@id="main"]/nav[@id="main-nav"]/ul/li[contains(@class, "product-range")]/div[contains(@class, "main-nav--level-container")]/ul/li/div/a'):
            yield response.follow(grocery_page, callback=self.grocery_parse)

    def grocery_parse(self, response):
        for product in response.xpath('//body//div[@id="main"]/section/article/div[contains(@class, "csc-default")]/div[@class="tx-aldi-products"]/div/a'):
            yield {
                'product-title': product.xpath('./div[@class="box m-text-image"]/div/div[contains(@class, "box--description")]/div[@class="box--description--header"]/text()').get().replace('\n', '').replace('\t', '')
            }
