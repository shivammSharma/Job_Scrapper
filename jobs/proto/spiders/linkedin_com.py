import scrapy
import os

class LinkedinComSpider(scrapy.Spider):
    name = "linkedin"
    allowed_domains = ["indeed.com"]



    custom_settings = {
         "FEEDS" : {
                 os.path.join("data", "ln.csv"): {
                'format': 'csv'
            }
        }
    }
    def start_requests(self):
            url = "https://indeed.com/"
            yield scrapy.Request(url, meta=dict(
                                 playwright=True,
                                 playwright_include_page=True,
                                
                             ))
            
    def parse(self, response):

        titles = response.css("div")
       
        for title in titles:
             
             yield{
                  "title": title.get()
             }
