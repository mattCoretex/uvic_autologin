import scrapy
import os
from getpass import *
from scrapy.http import FormRequest
from scrapy.http import Request
from scrapy.shell import inspect_response


class LoginSpider(scrapy.Spider):
    name = 'coursespaces'
    allowed_domains = ['www.uvic.ca']
    start_urls = ['https://www.uvic.ca/cas/login?service=https%3A%2F%2Fcoursespaces.uvic.ca%2Flogin%2Findex.php']

    custom_settings = {
        'FILES_STORE': os.getcwd(),
    }

    #UVIC CourseSpaces login
    def parse(self, response):
        usr = input("NetLinkID: ")
        pwd = getpass('Password: ')
        form = {'username':usr,'password':pwd}
        return FormRequest.from_response(response, formid='fm1', formdata=form, callback=self.parse_coursespaces)

    #get links to each active courses
    def parse_coursespaces(self, response):
        # link = response.xpath("//*[@class=' row card-deck']/div[@class='card mb-3 courses-view-course-item']/a/@href").extract()
        # - last 3 for irrelevent links
        link = response.xpath("//*[@class=' row card-deck']/div[@class='card mb-3 courses-view-course-item']/a/@href").extract()
        yield Request(link[0], callback=self.get_files, dont_filter=True)
        # print("\n\n\n\n\n\n\n%s\n\n\n\n\n\n" % req.url)
        # inspect_response(response,self)

    def get_files(self, response):
        files = response.xpath("//div[@class='activityinstance']/a/@href").getall()
        # for f in files:
        #     if('resource' in f):
        #         yield Request(url=f, callback=self.download_files, dont_filter=True)
        yield Request(url=files[1], callback=self.download_files, dont_filter=True)
        # inspect_response(response,self)


    def download_files(self, response):
        path = response.url.split('/')[-1]
        dirf = os.getcwd()
        if not os.path.exists(dirf):os.makedirs(dirf)
        os.chdir(dirf)
        with open(path, 'wb') as f:
            f.write(response.body)




