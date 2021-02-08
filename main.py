from requests_html import HTMLSession
from bs4 import BeautifulSoup

class Scraper():
    def __init__(self):
        self.session = HTMLSession()

    def scrape(self, URL):
        page = self.session.get(URL)
        soup = BeautifulSoup(page.html.html, "html.parser")

        # TItle, Category, 2 Sub Categories, Ad ID, Price, Price Unit, Tag, Description, Address, Location,
        primary_info_dict = {
            "Title": soup.find("title").string,
            "Sub Category 1": soup.find("span", {"itemprop": "category"}).string,
            "Price": soup.find("div", {"class": "jomcl-right"}).string[:-9],
            "Ad ID": soup.find("span", {"itemprop": "productID"}).string,
            "Description": soup.find("meta", {"property": "og:description"})["content"],
            "Category": "Vehicles",
            "Sub Category 2": "Used Motor Bikes",
            "Price Unit": "Millions",
            "Tag": "Sale",
            "Address": "",
            "Location": "Indonesia",
        }

        # Price Final Status, Year, Engine Size, Mileage, Transmission, Fuel type, Color Family, Edition, Listing ID
        secondary_info_name_list = [x.string for x in soup.findAll("span", {"itemprop": "name"})]
        secondary_info_value_list = [x.string for x in soup.findAll("span", {"itemprop": "value"})]
        secondary_info_dict = dict(zip(secondary_info_name_list, secondary_info_value_list))

        # 5 Full Size Image URLs
        images_list = [x["src"].replace("list", "gallery") for x in soup.findAll("img", {"itemprop": "image"})]
        images_dict = dict(zip({"Image Url 1", "Image Url 2", "Image Url 3", "Image Url 4", "Image Url 5"}, images_list))

        self.info = {**primary_info_dict, **secondary_info_dict, **images_dict}

url = "http://freelancer.homejobonline.in/index.php/all-adverts/advert/85503-yamaha-aerox-s-version"
scraper = Scraper()
scraper.scrape(url)

# print(scraper.info)
# print(scraper.info["Title"])
