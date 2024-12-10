import scrapy
import os

class Web3FullSpider(scrapy.Spider):

    name = "web3FullStack"
    allowed_domains = ["web3.career"]
    custom_settings = {
         "FEEDS" : {
                 os.path.join("data", "Web3Full.csv"): {
                'format': 'csv'
            }
        }
    }    
    def start_requests(self):
            url = "https://web3.career/full-stack-jobs"
            yield scrapy.Request(url, meta=dict(
                                 playwright=True,
                                 playwright_include_page=True,
                                
                             ))
    def parse(self, response):

        titles = response.xpath("/html/body/main/div/div[1]/div/div[3]/div[1]/table/tbody/tr")
        dis = response.xpath("/html/body/main/div/div[1]/div/div[3]/div[2]/turbo-frame/turbo-frame/div/div/div[2]/div[1]/div[2]")
        url = response.xpath("/html/body/main/div/div[1]/div/div[3]/div[1]/table/tbody/tr/td/div/div/div/a/@href")

        count = 1

        for title in titles:
             tits = title.xpath("./td/div/div/div/a/h2/text()").extract()
             salary = title.xpath("./td[5]/p/text()").extract()
             date = title.xpath("./td[3]/time/text()").extract()
             company = title.xpath("./td[2]/a/h3/text()").extract()
             tags = title.xpath("./td[6]/div/span/a/text()").extract()
             img = 'https://web3-recruit.com/____impro/1/onewebmedia/Web3%20logo.png?etag=W%2F%227735-63111110%22&sourceContentType=image%2Fpng&ignoreAspectRatio&resize=300%2B300'

             medium = title.xpath("./td[4]/a/text()").extract() or title.xpath("./td[4]/p/text()").extract()
             url = title.xpath("./td/div/div/div/a/@href").extract()
             job_url = f"https://web3.career/full-stack-jobs{url[0]}"
             follow_next_page = f"https://web3.career/full-stack-jobs/?page={count}"
             count += 1
             yield{
                  "title": tits,
                  "date": date,
                  "company": company,
                  "location": medium,
                  'tags': tags,
                  "url": job_url,
                  "salary": salary,
                  'img': img,
                  'description': 'N/A'
             }
             if count != 2:
                yield response.follow(follow_next_page, self.parse)
        

             
             


