import scrapy


class HttpBinSpider(scrapy.Spider):
    name = 'httpbinspider'
    allowed_domains = ['httpbin.org']

    def start_requests(self):
        for i in range(1, 16):
            yield scrapy.FormRequest(url='http://httpbin.org/get', callback=self.first, dont_filter=True)

    def first(self, response):
        text = response.text
        print('-------------------------------------------------------------------------------------------------')
        print(text)
        print('-------------------------------------------------------------------------------------------------')
        yield text
