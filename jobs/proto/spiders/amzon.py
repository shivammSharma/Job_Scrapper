import scrapy


class AmazonjobsSpider(scrapy.Spider):
    custom_settings = {
    'FEEDS': {
    'amazon_jobs.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'indent': 4,
        'overwrite': True,  
    }
    }
    }



    name = "amazonJobs"
    allowed_domains = ["amazon.jobs"]
    
    def start_requests(self):
            url = "https://www.amazon.jobs/en/job_categories"
            yield scrapy.Request(url, meta=dict(
                                 playwright=True,
                                 playwright_include_page=True,
                                
                             ))

    def parse(self, response):
        titles = response.xpath("/html/body/div[2]/div[1]/div[4]/div[2]/div/div/div/div")
                 
        for title in titles:
            relative_url = title.xpath("./a/@href").extract()
            absolute_url = f"https://amazon.jobs{relative_url[0]}"
            types = title.xpath("./a/div/div[1]/h3/text()").extract()

            
            yield {
                'type': types,
                'url': absolute_url, 
            }
            
          
class AmazonDataScience(scrapy.Spider):
     name = "amazonDataScience"
     allowed_domain = ['amazon.jobs']

     def start_requests(self):
            url = "https://www.amazon.jobs/content/en/job-categories/data-science"
            yield scrapy.Request(url, meta=dict(
                                 playwright=True,
                                 playwright_include_page=True,
                                
                             ))

     def parse(self, response):
        titles = response.xpath("/html/body/div[1]/div[2]/div/main/div[2]/div/div[2]/ul/li/div/div/div/div/div/div")
                 
        for title in titles:
            tits = title.xpath("./span/text()").extract()

            
            yield {
                'url': tits,
            }
