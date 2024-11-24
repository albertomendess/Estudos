from scrapy import Spider, Request

class ArticleSpider(Spider):
    name = 'article'

    def star_requests(self):
        urls = [
            'http://en.wikipedia.org/wiki/Python_%28programming_language%29',
            'https://en.wikipedia.org/wiki/Functional_programming',
            'https://en.wikipedia.org/wiki/Monty_Python'
        ]
        return [Request(url= url,
                        callback= self.parse) for url in urls]
    
    def parse(self, response):
        url     = response.url
        title   = response.css('h1::text').extract_first()
        print(f"URL is: {url}")
        print(f"Title is: {title}")
