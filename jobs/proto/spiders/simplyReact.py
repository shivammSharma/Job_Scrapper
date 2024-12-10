import scrapy
import os

class SimplyReactSpider(scrapy.Spider):
    name = "simplyReact"
    allowed_domains = ["simplyhired.com"]
    custom_settings = {
         "FEEDS" : {
                 os.path.join("data", "ReactJobs.csv"): {
                'format': 'csv'
            }
        }
    }

        
    start_urls = [
        "https://www.simplyhired.com/search?q=react+developer&l=Us",
        "https://www.simplyhired.com/search?q=react+developer&l=Us&cursor=ABQAAgAoAAAAAAAAAAAAAAACOTEYrwEBAQ8A3qQloJr6Qr8PDlJ4IXYGo2T5ahCqdVIHq4Wy4esJi7D2wBoJ%2FrqMmLuwAfkpNrOl9tVXQoWm2LgiDPnJD9EXXxYFxCzmCsbrnUs2lR5%2F7DA%2FH9xt5Q%3D%3D",
        "https://www.simplyhired.com/search?q=react+developer&l=Us&cursor=ABQAAQAUAAAAAAAAAAAAAAACOTEYrwEBAQY3O4kA4RCZ7XByTKuqOXysubdW030zu6iJ%2FVzbMsOlL4%2BJ8rictu1moxXh1IpzFA%3D%3D",
        "https://www.simplyhired.com/search?q=react+developer&l=Us&cursor=ABQAAwA8AAAAAAAAAAAAAAACOTEYrwEBAQ8Amh2%2FFl9ZQB2D6zGXh6PbGAgD28Nr5h3aXuwD8TbFNZg00u3FyYMtqXYcZL881QZjmQkJAVYVn6qfNRdCwkL8soV2L5bErEnALa2Q3IFQakX73NtuDHdYYF9OBCmIrPhosnjRI5QE7jprBD%2FRtU8CGb2pQ5%2Bt",
        "https://www.simplyhired.com/search?q=react+developer&l=Us&cursor=ABQABQBkAAAAAAAAAAAAAAACOTEYrwEFARAiDzAOIgY2BiNMNZnXjB4c8qkaDD08jU7Ba8aXnSVbHWW6leLGZjrblEHdfdin4rAo2YIsjkMPA7l1ZLmjxjy6eyRmG4wK77YWR2ceRKTltr1ZTygtqU6NUFhVjsqZTuMMIfRtBNwJ4kpnavumiH6EA19CCgEoarHRmVnDIB9syGQPiub7Odq%2FPsgSvlIJzVhPZ%2BgLGGfHhYO4s8bpnAkp",
        "https://www.simplyhired.com/search?q=react+developer&l=Us&cursor=ABQABgB4AAAAAAAAAAAAAAACOTEYrwEFARAiEDAOIgg6BhQPLj%2BU5PWOIyjPfcsv30tMDTuIv1qORPghTTILNQmgBBuw43sk8VW3sFB1D9K%2FP3GtHpPAoo7qHrxxTqgD1oXIf%2BmlMkZDEjNxOjb4rL44uAyTgMA3kTzljr8RWtcMWlJ5qcNjNYhJC9bIUoTu%2BGFjZIJiEriwsTTa20o6gyQ4K5ZABg6gFfZAqelHn41cjTbaOZK4CymK1y2caU3m4QRkp%2FR2ff5DQ1%2Be",
        "https://www.simplyhired.com/search?q=react+developer&l=Us&cursor=ABQABwCMAAAAAAAAAAAAAAACOTEYrwEFARAiECwRJgg8BgIq3xTS5iAlz289i67o84DAkfc4UmJPpybJuAqthIXux89ZpwT5q8gfMsSE8fj%2F7aSzn7LaDf9dHmDns9%2FysBYJYwxyouLB7VBmqmUn%2BBdfxDQ7L0TT4Ipa6byglUuDtHUAbUqTrcunkCfHeZ%2FG74u0eXE%2BPXEh5h8aSBsNjYYXh2uksh79NHm1wg9XTrn1g7sCrX3i%2BhUuMyjheZVWTDhd6Gr4rLLpvqB4rOZSnUE7Ts1Eif03fKhBtK1QQw%3D%3D",
        "https://www.simplyhired.com/search?q=react+developer&l=Us&cursor=ABQACACgAAAAAAAAAAAAAAACOTEYrwEEASFGFzAIQgYgpJxAJa9Zu0oaVM9i56KoP7mvHGB7yU%2Bshg8IOKPFczPfNWXg4fUmuL9i0fuJLJ1GOJ0Po7yudpYeU9MLFK67Lax55CMW%2FaGd2lugSIsf%2FSoDMejtTHVfdj9jZxqS9DDqxAIJI5ruMDITvt7ZGrvYNv5HuoLA2LhocoxIakivy1fZylt5OoM83%2BwBU9Ylqs9etmBVNYQ1%2Bh6GBEb%2BnMffD1X820xM%2BBUcv7cDIcuOYl4sGVzMNJCp7NfeMa138tKbKPdytQPu",
        "https://www.simplyhired.com/search?q=react+developer&l=Us&cursor=ABQACQC0AAAAAAAAAAAAAAACOTEYrwEEASFEGDIIQgcQjHcC7WQhMMNVXBUi3egZ3iMnU%2FH9aoZ7YphrIk%2BSHUNs3Kyd5tokHE76a%2FMF5M0sZRX3Z4ySuv1Xac5OT4LmaOWakkDJhaP9QXnml%2BDGxnWLAy5gMeykTQTMybN0zgRL5gv0mkcLKIFMFexPjatjwaYb%2BcrkEACyMWe2pFUBWhPDWry1hWIJxR%2FTOCY18SUkBfXUt7B4X1A6ZmhSSX4smw43ZVQBbB0FGfD9MrBHtpsvox6axtUoXrJxurA6pUFAf%2BZonvuO6BXegQcB%2Fm5E%2BPI%3D",
        "https://www.simplyhired.com/search?q=react+developer&l=Us&cursor=ABQACgDIAAAAAAAAAAAAAAACOTEYrwEEASFEGDIIQgcg5ZFtyZKw481ycgZsxh9qBZvnlR8vzr359qlByrUYl46dYHgSKoxBdsjVhk1quxaovuhRQOP4UfVyhRHSlQAXAmT2%2F4xOWdnfCwAtY%2Fjjq77eXZa0EktEUDXP1bygPyuu4iuFYB0XhLC1EwE48aQ4qrwmrrEs76a94KMHKWI580pu5cuf7H2pF1QD%2FrblcUaJP%2FoGfg%2F92rteRx5z4pSDwTc35QcfCIaWFWbs2JTFAlFKe2OoqYtmoXcQ7HxuE%2Bd%2BLx2sF7gJECQj5BAoQOUlQnki1N41Z3Vq%2BDI%3D0",
        "https://www.simplyhired.com/search?q=react+developer&l=Us&cursor=ABQACwDcAAAAAAAAAAAAAAACOTEYrwEDASFEIXQHEB2waN80vbsDbEZfCh2xOxB3gwQrKiMWNcbgE86vnVuNBMqYndE%2F15h%2FiT4Bgav1K0aOMOZrLShKXskOFx91oiuEeBQENH6JrAQlktp5McOHovaI4z7A6LDXaZjsIqe2hjouk5uShKLeiz37n1O8yAI5oUt7nS4CfDw0%2F2f13iZKAEvlnoVB%2FuuKJuMRAP1BexjNHMCm9%2BRqw1H6i2k1STGTLq6c9loHj0%2Fk4PW4h7PJ5am6FCKU3dMPeBfMTsfrsrBTZ%2BB5J9FOub4QxxERT5NAg0HmgnJh9cx9iXMz1m4DOr%2FITRE%3D"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta=dict(
                    playwright=True,
                    playwright_include_page=True,
                )
            )

    def parse(self, response):
        titles = response.css("div.css-obg9ou")
        for title in titles:
            tl = title.css("div.chakra-stack.css-1igwmid h2 a::attr(href)").get()
            description = title.css("p.chakra-text.css-jhqp7z::text").get()
            date = title.css("div.css-2imjyh p.chakra-text.css-5yilgw::text").get()
            salary = title.css("div.css-2imjyh p.chakra-text.css-1g1y608::text").get()
            location = title.css("p.chakra-text.css-1sawo7p span.css-1t92pv::text").get()
            company = title.css("p.chakra-text.css-1sawo7p span.css-lvyu5j span::text").get()
            url = f"https://www.simplyhired.com/{tl}"
            yield {
                "title": title.css("div.chakra-stack.css-1igwmid h2 a::text").get(),
                "url": url,
                "description": description,
                "date": date,
                "salary": salary,
                "location": location,
                'company': company,
                'img': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fglobalcybersecuritynetwork.com%2Fcareer%2Fsimplyhired%2F&psig=AOvVaw2pYpM31MSM-RSaPPAJYHrY&ust=1733255682947000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLi2mdzuiYoDFQAAAAAdAAAAABAE'

            }