from requests_html import HTMLSession
from bs4 import BeautifulSoup

class AdvertScraper():
    def __init__(self):
        self.data = []

    def scrape(self, URL=""):
        session = HTMLSession()
        page = session.get(URL)
        soup = BeautifulSoup(page.html.html, "html.parser")

        title = soup.find("title").string
        category_0 = "6" # "Vehicles"
        category_1 = "32" # soup.find("span", {"itemprop": "category"}).string
        category_2 = "33" # "Used Motor Bikes"
        price_string = soup.find("div", {"class": "jomcl-right"}).string
        price = price_string[:-9] if price_string is not None else "0"
        currency = "Millions"
        tag_id = "1" # "Sale"
        description = soup.find("meta", {"property": "og:description"})["content"]
        address = "."
        location = "33" # "Indonesia"
        user_id = soup.find("input", {"id": "userid"})["value"]
        ad_id = soup.find("span", {"itemprop": "productID"}).string

        more_details_name_list = [x.string for x in soup.findAll("span", {"itemprop": "name"})]
        more_details_value_list = [x.string for x in soup.findAll("span", {"itemprop": "value"})]
        image_urls_list_dirty = soup.findAll("img", {"itemprop": "image"})
        image_urls_list = [x["src"].replace("list", "gallery") for x in image_urls_list_dirty] if len(image_urls_list_dirty) > 0 else ["."]*5

        more_details_dict = dict(zip(more_details_name_list, more_details_value_list))
        image_urls_dict = dict(zip({"Image Url 1", "Image Url 2", "Image Url 3", "Image Url 4", "Image Url 5"}, image_urls_list))

        self.data = [
            ("title", title),

            ("category[]", category_0),
            ("category[]", category_1),
            ("category[]", category_2),

            ("exf_26", more_details_dict["Price Final Status"]),
            ("exf_27", more_details_dict["Year"]),
            ("exf_28", more_details_dict["Engine Size"]),
            ("exf_29", more_details_dict["Mileage"]),
            ("exf_31", more_details_dict["Fuel type"]),
            ("exf_32", more_details_dict["Color Family"]),
            ("exf_33", more_details_dict["Edition"]),
            ("exf_34", more_details_dict["Listing ID"]),
            ("exf_35", ad_id),

            ("exf_36", image_urls_dict["Image Url 1"]),
            ("exf_37", image_urls_dict["Image Url 2"]),
            ("exf_38", image_urls_dict["Image Url 3"]),
            ("exf_39", image_urls_dict["Image Url 4"]),
            ("exf_40", image_urls_dict["Image Url 5"]),

            ("exf_42", more_details_dict["Transmission"]),

            ("price", price),
            ("currency", currency),
            ("tagid", tag_id),

            ("description", description),
            ("address", address),
            ("location[]", location),

            ("topaddays", ""),
            ("privacy[]", "on"),
            ("mode", "new"),
            ("extImages", ""),

            ("userid", user_id),
            ("id", ad_id),

            ("latitude", ""),
            ("langtitude", ""),
            ("defLocation", "USA"),
            ("7d3479d3294d40d3e0bc24756b522bd5", "1"),
        ]

        return self.data

advert_scraper = AdvertScraper()
advert_scraper.scrape(URL="https://freelancer.homejobonline.in/index.php/all-adverts/advert/85503-yamaha-aerox-s-version")
print(advert_scraper.data)
