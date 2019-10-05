# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import FormRequest

class LoginSpider(scrapy.Spider):
    name = 'uvic'
    allowed_domains = ['uvic.ca']
    start_urls = ['https://www.uvic.ca/']
    coursespaces_url = ['https://coursespaces.uvic.ca/']

    def parse(self, response):
        login_page = response.xpath('//*[@class="glbl__lnk glbl__lnk--signin glbl__lnk--icon glbl__lnk--unauth"]/@href').extract_first()
        absolute_login_page_url = response.urljoin(login_page)
        yield FormRequest(absolute_login_page_url,
            formdata={ 'username': 'foo', 'password': 'bar'}, callback=self.parse_page2)

    def parse_page2(self, response):
        coursespaces_url = 'https://coursespaces.uvic.ca/'
        yield FormRequest(coursespaces_url)


    def parse_after_login(self, response):
    	if response.xpath('//a[text()="Logout"]'):
    		self.log("You logged in")

    # def parse_cs(self, response, start_urls):
    #   yield dict(
    #     main_url=s,
    #     other_url=response.url,
    #     foo=foo,
    # )

"""
def parse_page2(self, response, main_url, foo):
    yield dict(
        main_url=main_url,
        other_url=response.url,
        foo=foo,
    )
"""
