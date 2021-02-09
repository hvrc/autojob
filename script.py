from requests_html import HTMLSession
from bs4 import BeautifulSoup

class Scraper():
    def __init__(self):
        self.items_per_page = 6
        self.data = []

    def get_adverts_links(self, URL, number_of_pages):
        links = []

        for current_page in range(number_of_pages):
            session = HTMLSession()
            page = session.get(URL)
            soup = BeautifulSoup(page.html.html, "html.parser")

            advert_link_prefix = "https://freelancer.homejobonline.in/index.php/all-adverts/advert/"
            connector = "?start="

            links_on_current_page = [advert_link_prefix + str(x["onclick"][56:-1]) for x in soup.findAll("img", {"itemprop": "image"})]

            URL = str(URL + connector + str(self.items_per_page*(current_page+1)))

            links.extend(links_on_current_page)

        return links

    def scrape_adverts_data(self, URL, number_of_pages):
        for link in self.get_adverts_links(URL, number_of_pages):
            session = HTMLSession()
            page = session.get(link)
            soup = BeautifulSoup(page.html.html, "html.parser")

            advert_link = link
            category = "Vehicles"
            sub_category_2 = "Used Motor Bikes"
            price_unit = "Millions"
            tag = "Sale"
            address = ""
            location = "Indonesia"

            title = soup.find("title").string
            sub_category_1 = soup.find("span", {"itemprop": "category"}).string
            price_string = soup.find("div", {"class": "jomcl-right"}).string
            price = price_string[:-9] if price_string is not None else "0"
            ad_id = soup.find("span", {"itemprop": "productID"}).string
            description = soup.find("meta", {"property": "og:description"})["content"]
            more_details_name_list = [x.string for x in soup.findAll("span", {"itemprop": "name"})]
            more_details_value_list = [x.string for x in soup.findAll("span", {"itemprop": "value"})]
            image_urls_list = [x["src"].replace("list", "gallery") for x in soup.findAll("img", {"itemprop": "image"})]

            # Advert Link, Title, Category, 2 Sub Categories, Ad ID, Price, Price Unit, Tag, Description, Address, Location,
            details_dict = {
                "Advert Link": link,
                "Title": title,
                "Sub Category 1": sub_category_1,
                "Price": price,
                "Ad ID": ad_id,
                "Description": description,
                "Category": category,
                "Sub Category 2": sub_category_2,
                "Price Unit": price_unit,
                "Tag": tag,
                "Address": address,
                "Location": location,
            }

            # Price Final Status, Year, Engine Size, Mileage, Transmission, Fuel type, Color Family, Edition, Listing ID
            more_details_dict = dict(zip(more_details_name_list, more_details_value_list))

            # 5 Full Size Image URLs
            image_urls_dict = dict(zip({"Image Url 1", "Image Url 2", "Image Url 3", "Image Url 4", "Image Url 5"}, image_urls_list))

            self.data.append({**details_dict, **more_details_dict, **image_urls_dict})

scraper = Scraper()
scraper.scrape_adverts_data(
    URL="https://freelancer.homejobonline.in/index.php/category/31",
    number_of_pages=2
)

print(scraper.data)
