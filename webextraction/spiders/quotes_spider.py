import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.dictionary.com/browse/blog',
            'https://en.wikipedia.org/wiki/Web_scraping',
            'https://www.lexico.com/en/english-thesaurus',
            'https://www.panresearch.ie/services/website-user-testing.293.html',  
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
#'https://en.wikipedia.org/wiki/Web_scraping',
