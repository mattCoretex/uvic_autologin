# -*- coding: utf-8 -*-

"""
 scrapy crawl myspider -a category=electronics -a domain=system
class MySpider(scrapy.Spider):
    name = 'myspider'

    def __init__(self, category='', **kwargs):
        self.start_urls = [f'http://www.example.com/{category}']  # py36
        super().__init__(**kwargs)  # python3

    def parse(self, response)
        self.log(self.domain)  # system

"""

"""
 response.xpath('//*[@class="login"]').extract_first()

"""


import scrapy

from getpass import *
from scrapy.http import FormRequest
from scrapy.shell import inspect_response

usr = input("NetLinkID: ")
pwd = getpass('Password: ')

class LoginSpider(scrapy.Spider):
    name = 'uvic'
    allowed_domains = ['uvic.ca']
    start_urls = ['https://www.uvic.ca/']
    coursespaces_url = ['https://coursespaces.uvic.ca/']

    def parse(self, response):
        login_page = response.xpath('//*[@class="glbl__lnk glbl__lnk--signin glbl__lnk--icon glbl__lnk--unauth"]/@href').extract_first()
        absolute_login_page_url = response.urljoin(login_page)
        yield FormRequest(absolute_login_page_url,
            formdata={ 'username': usr, 'password': pwd}, callback=self.parse_coursespaces)

    def parse_coursespaces(self, response):
        coursespaces_url = 'https://coursespaces.uvic.ca/'
        yield FormRequest(coursespaces_url, callback=self.parse_inspection)

    def parse_inspection(self, response):
        inspect_response(response, self)



    def parse_after_login(self, response):
    	if response.xpath('//a[text()="Logout"]'):
    		self.log("You logged in")









