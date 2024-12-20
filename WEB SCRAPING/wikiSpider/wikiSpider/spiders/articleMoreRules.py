from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules = [
        Rule(
            LinkExtractor(allow= '(/wiki/)((?!:).)*?'),
            callback= 'parse_items',
            follow= True,
            cb_kwargs= {'is_article' : True}
        ),
        Rule(
            LinkExtractor(allow= '.*'),
            callback= 'parse_items',
            cb_kwargs= {'is_article' : False}
        )
    ]
    
    def parse_items(self, response, is_article):
        print(response.url)
        title = response.css('span.mw-page-title-main::text').extract_first()
        if is_article:
            url = response.url
            text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
            lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
            lastUpdated = lastUpdated.replace('This page was last edited on ', '')
            print(f"URL is: {url}")
            print(f"Tile is: {title}")
            print(f"Text is: {text[:100]}")
        else:
            print(f"This is not an article: {title}")