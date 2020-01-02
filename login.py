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
        yield Request(link[0], callback=self.parse_file_list, dont_filter=True)

    def parse_file_list(self, response):
        files = response.xpath("//div[@class='activityinstance']/a/@href").getall()
        for f in files[1:5]:
            if('resource' in f):
                yield Request(url=f, callback=self.get_file_link, dont_filter=True)
        # print("\n\n\n\n\n\n\n%s\n\n\n\n\n\n" % f)

    def get_file_link(self, response):
        file_link = response.xpath("//div[@class='resourceworkaround']/a/@href").extract()
        yield Request(url=file_link[0], callback=self.download, dont_filter=True)


    def download(self, response):
        path = response.url.split('/')[-1]
        self.logger.info('Saving PDF %s', path)
        with open(path, 'wb') as f:
            f.write(response.body)
        # path = response.url.split('/')[-1]
        # dirf = os.getcwd() + '/course'
        # if not os.path.exists(dirf):os.makedirs(dirf)
        # os.chdir(dirf)
        # with open(path, 'wb') as f:
        #     f.write(response.body)
        # inspect_response(response,self)





