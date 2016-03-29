import scrapy

class DmozSpider(scrapy.Spider):
    name = "coding-cal"
    allowed_domains = [
        "codechef.com",
        "codeforces.com"
    ]

    start_urls = [
        "https://www.codechef.com/contests/",
        "http://codeforces.com/contests"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="table-questions"][1]/table/tr'):
            title = sel.xpath('td[2]/a/text()').extract()
            link = sel.xpath('td[2]/a/@href').extract()
            desc = sel.xpath('td[1]/text()').extract()
            print desc, title, link
            print '\n'

        for sel in response.xpath('//div[@class="datatable"][1]/div/table/tr'):
            #title = sel.xpath('td[2]/a/text()').extract()
            #link = sel.xpath('td[2]/a/@href').extract()
            desc = sel.xpath('td[1]/text()').extract()
            print desc #, title, link
            print '\n'
