import scrapy


class GrocerySpider(scrapy.Spider):
    name = 'grocery_products'

    start_urls = ['https://www.aldi.com.au/']
    
    def process_price(product_price_value, product_price_decimal):
        if product_price_value and product_price_decimal:
            return product_price_value + product_price_decimal
        elif not product_price_decimal and product_price_value:
            return product_price_value + 'c'
        else:
            return None

    def parse(self, response):
        yield from response.follow_all(xpath='//body//div[@id="main"]/nav[@id="main-nav"]/ul/li[contains(@class, "product-range")]/div[contains(@class, "main-nav--level-container")]/ul/li/div/a', callback=self.grocery_parse)

    def grocery_parse(self, response):
        products = response.xpath('//body//div[@id="main"]/section/article//div[@class="tx-aldi-products"]/div/a/div[@class="box m-text-image"]/div')
        if len(products) == 0:
            yield from response.follow_all(xpath='//body//div[@id="main"]/section/article/div[@class="csc-default"]/div/div/div[contains(@class, "csc-textpic-imagerow")]/div[contains(@class, "csc-textpic-imagecolumn")]/a', callback=self.grocery_parse)
        else:
            for product in products:
                product_title_raw = product.xpath('./div[contains(@class, "box--description")]/div[@class="box--description--header"]/text()').getall()
                product_price_value = product.xpath('./div[contains(@class, "box--description")]/div[@class="box--price"]/span[@class="box--value"]/text()').get()
                product_price_decimal = product.xpath('./div[contains(@class, "box--description")]/div[@class="box--price"]/span[@class="box--decimal"]/text()').get()
                yield {
                    'product_title': ''.join(product_title_raw).strip('\n\t '),
                    'product_image': product.xpath('./div[contains(@class, "box--image-container")]/img/@src').get(),
                    'packsize': product.xpath('./div[contains(@class, "box--description")]/div[@class="box--price"]/span[@class="box--amount"]/text()').get(),
                    'price': self.process_price(product_price_value, product_price_decimal),
                    'price_per_unit': product.xpath('./div[contains(@class, "box--description")]/div[@class="box--price"]/span[@class="box--baseprice"]/text()').get(),
                }


