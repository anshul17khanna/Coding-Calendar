import scrapy

countt = 0

class coding_calSpider(scrapy.Spider):
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
        flag = 0
        global countt
        for sel in response.xpath('//div[@class="table-questions"][1]/table/tr'):
            codename = sel.xpath('td[1]/text()').extract_first()
            name = sel.xpath('td[2]/a/text()').extract_first()
            st = sel.xpath('td[3]/text()').extract_first()
            et = sel.xpath('td[4]/text()').extract_first()
            link = sel.xpath('td[2]/a/@href').extract_first()
            if codename and name and link:
                if flag is 0:
                    flag = 1
                    #print '====== CODECHEF ======'
                countt+=1
                link = "https://www.codechef.com"+str(link)
                print codename+'\n', name+'\n',
                print 'Start : '+st+'\n', 'End : '+et+'\n', "Link : "+link+'\n'
        if flag is 0:
            pass # print '====== CODECHEF ======'
            # print 'No Contest at Present! :('

        for sel in response.xpath('(//div[@class="datatable"])[1]/div/table/tr'):
            # title = sel.xpath('td[2]/a/text()').extract()
            name = sel.xpath('td[1]/text()').extract_first()
            st = sel.xpath('td[3]/a/span/text()').extract_first()
            dur = str(sel.xpath('td[4]/text()').extract_first()).strip( )
            link = 'http://codeforces.com/contests' # sel.xpath('@data-contestId').extract_first()
            if name:
                countt+=1
                print name+'\n', 'Start : '+st+'\n', 'Duration : '+dur+'\n', 'Link : '+link+'\n'

        print str(countt) + ' Contest(s) found!\n'


# scrapy crawl coding-cal -o crap.json -t json 2> crap.text
# scrapy crawl coding-cal 2> crap.text
