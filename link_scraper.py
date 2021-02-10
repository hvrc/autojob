from requests_html import HTMLSession
from bs4 import BeautifulSoup

class LinkScraper():
    def __init__(self):
        self.items_per_page = 6
        self.links = []
        # self.cars_parts_link = "https://freelancer.homejobonline.in/index.php/cars-parts"
        # self.used_cars_link = "https://freelancer.homejobonline.in/index.php/category/33-used-cars"
        # self.motor_bikes_link = "https://freelancer.homejobonline.in/index.php/category/31-motor-bikes"
        # self.houses_for_rent = "https://freelancer.homejobonline.in/index.php/houses-flats-for-rent"

    def scrape(self, URL, number_of_pages=1):
        for current_page in range(number_of_pages):
            session = HTMLSession()
            page = session.get(URL)
            soup = BeautifulSoup(page.html.html, "html.parser")

            advert_link_prefix = "https://freelancer.homejobonline.in/index.php/all-adverts/advert/"
            connector = "?start="

            links_on_current_page = [advert_link_prefix + str(x["onclick"][56:-1]) for x in soup.findAll("img", {"itemprop": "image"})]
            URL = str(URL + connector + str(self.items_per_page*(current_page+1)))
            self.links.extend(links_on_current_page)

link_scraper = LinkScraper()
link_scraper.scrape(
    URL="https://freelancer.homejobonline.in/index.php/category/31-motor-bikes",
    number_of_pages=1,
)
print(link_scraper.links)
