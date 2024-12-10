import scrapy
import os
class InternshipWebSpider(scrapy.Spider):
    name = "internship"
    allowed_domains = ["internshala.com"]
    custom_settings = {
         "FEEDS" : {
                 os.path.join("data", "WebInternship.csv"): {
                'format': 'csv'
            }
        }
    }

    def start_requests(self):
                url = "https://internshala.com/internships/web-development-internship/"
                yield scrapy.Request(url, meta=dict(
                                    playwright=True,
                                    playwright_include_page=True,
                                    
                                ))
    def parse(self, response):
            count =1
            
            titles = response.css("div.container-fluid.individual_internship.view_detail_button.visibilityTrackerItem")
            u = response.css("div div.container-fluid.individual_internship::attr(data-href)")
            b=0
            for title in titles:
                    tt = title.css("div.internship_meta.duration_meta")
                    t = tt.css("div div h3 a::text").get()
                    company = tt.css("div div div div p::text").get()
                    location = tt.css("div.individual_internship_details div div span a::text").get()
                    salary = tt.css("div.individual_internship_details div.detail-row-1 div span.stipend::text").get()
                    date = tt.css("div.individual_internship_details div.detail-row-2 div div span::text").get()
                    img = tt.css("div.internship_logo img::attr(src)").get()
                    url = title.css("div.container-fluid.individual_internship::attr(data-href)").get()

                    follow_next_page = f"https://internshala.com/internships/web-development-internship/page-{count}/"
                    count+=1
                    b+=1
                    yield{
                            'title': t,
                            'date': date,
                            "company": company,
                            'location': location,
                            'tags': 'N/A',
                            'url': f"https://internshala.com{url}",
                            'salary': salary,
                            'img': img,

                    }
                    
                    if count !=2:
                        yield response.follow(follow_next_page, self.parse)

            for url in u:
                yield response.follow(url.get(), self.parse_des)

    def parse_des(self, response):
           descriptions = response.css("div.detail_view")
           
           for d in descriptions:
                dd = d.css("div.text-container::text").getall()
                yield{
                        "description": dd,
                }