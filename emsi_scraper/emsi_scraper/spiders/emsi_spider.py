import scrapy
from scrapy.crawler import CrawlerProcess
import json

class EmsiSpider(scrapy.Spider):
    name = "economic_modeling"
    start_urls = [
            'https://api.lever.co/v0/postings/economicmodeling?group=team&mode=json'
        ]

    def parse(self, response):
        json_response = json.loads(response.text)
        for team in json_response:
            postings = team['postings']
            for post in postings:
                yield {
                    "team": post['categories']['team'],
                    "commitment": post['categories']['commitment'],
                    "location": post['categories']['location'],
                    "department": post['categories']['department'],
                    "id": post['id'],
                    "title": post['text'],
                    "url": post['hostedUrl'],
                    "description": post['descriptionPlain'],
                    "responsibilities": post['lists'][0]['content'],
                    "1requirements": post['lists'][1]['content']

                }

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'json',
    'FEED_URI': 'output.json',
})

process.crawl(EmsiSpider)
process.start()