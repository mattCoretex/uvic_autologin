# -*- coding: utf-8 -*-
import scrapy
import sys

from scrapy.http import FormRequest

# netlinkid = sys.argv[1]
# password = sys.argv[2]

class LoginSpider(scrapy.Spider):
    name = 'uvic'
    allowed_domains = ['uvic.ca']
    start_urls = ['https://www.uvic.ca/']

    def parse(self, response):
        login_page = response.xpath('//*[@class="glbl__lnk glbl__lnk--signin glbl__lnk--icon glbl__lnk--unauth"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(login_page)
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': username, 'password': password}
        )
        # yield scrapy.Request(absolute_next_page_url)
    	# formdata={'csrf_token': csrf_token,
    	# 			'username': 'foo',
    	# 			'password': 'bar'}, callback=self.parse_after_login)

        # yield FormRequest('absolute_next_page_url')
    	# csrf_token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
     #    yield FormRequest('http://quotes.toscrape.com/login', 

    def parse_after_login(self, response):
    	if response.xpath('//a[text()="Logout"]')
    		self.log("You logged in")







