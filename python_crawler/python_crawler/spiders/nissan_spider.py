import scrapy


class NissanSpider(scrapy.Spider):
    name = "dongfeng-nissan"
    allowed_domains = ["dongfeng-nissan.com"]
    start_urls = [
        "https://www.dongfeng-nissan.com.cn/buy/services/Maintenance",
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
