import scrapy
from getpass import *
from scrapy.http import FormRequest
from scrapy.http import Request
from scrapy.shell import inspect_response


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
        # - last 3 for irrelevent links
        link = response.xpath("//*[@class=' row card-deck']/div[@class='card mb-3 courses-view-course-item']/a/@href").extract()
        req = Request(link[0], callback=self.parse_inspection)
        print("\n\n\n\n\n\n\n%s\n\n\n\n\n\n" % req.url)
        inspect_response(response,self)

    def parse_inspection(self, response):
        inspect_response(response,self)




