import scrapy
import os
from getpass import *
from scrapy.http import FormRequest
from scrapy.http import Request
from scrapy.shell import inspect_response
import urllib.parse


class LoginSpider(scrapy.Spider):
    name = 'coursespaces'
    allowed_domains = ['www.uvic.ca']
    start_urls = ['https://www.uvic.ca/cas/login?service=https%3A%2F%2Fcoursespaces.uvic.ca%2Flogin%2Findex.php']

    #UVIC CourseSpaces login
    def parse(self, response):
        usr = input("NetLinkID: ")
        pwd = getpass('Password: ')
        form = {'username':usr,'password':pwd}
        return FormRequest.from_response(response, formid='fm1', formdata=form, callback=self.parse_coursespaces)

    #get links to each active courses
    def parse_coursespaces(self, response):
        # link = response.xpath("//*[@class=' row card-deck']/div[@class='card mb-3 courses-view-course-item']/a/@href").extract()
        # link = response.xpath("//*[@class=' row card-deck']/div[@class='card mb-3 courses-view-course-item']/a/@href").extract()
        # - last 3 links are irrevelent and shall be ignored
        for course in response.xpath("//*[@class=' row card-deck']/div[@class='card mb-3 courses-view-course-item']/a/@href").extract()[0:-3]:
            yield Request(course, callback=self.parse_file_list, dont_filter=True)

    #prepare all links to each file for download
    def parse_file_list(self, response):
        folder_name = response.xpath("//div[@id='page-navbar']/nav/ol/li/a/@title").extract()[0]
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        for f in response.xpath("//div[@class='activityinstance']/a/@href").getall():
            if('resource' in f):
                yield Request(url=f, callback=self.get_file_link,meta={'folder':folder_name}, dont_filter=True)

    #prepare individual link for download
    def get_file_link(self, response):
        file_link = response.xpath("//div[@class='resourceworkaround']/a/@href").extract()
        yield Request(url=file_link[0], callback=self.download,meta={'folder':response.meta.get('folder')}, dont_filter=True)

    def download(self, response):
        path = os.getcwd() + "/" + response.meta.get('folder')
        filename = response.url.split('/')[-1]
        filename = urllib.parse.unquote(filename).replace(" ", "_")
        path = path + "/" + filename
        self.logger.info('\n\n\tSaving PDF %s\n\n', path)
        with open(path, 'wb') as f:
            f.write(response.body)

