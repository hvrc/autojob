from requests_html import HTMLSession
from bs4 import BeautifulSoup

class Scraper():
    def __init__(self):
        self.items_per_page = 6
        self.links = []
        self.data = []
        # self.cars_parts_link = "https://freelancer.homejobonline.in/index.php/cars-parts"
        # self.used_cars_link = "https://freelancer.homejobonline.in/index.php/category/33-used-cars"
        # self.motor_bikes_link = "https://freelancer.homejobonline.in/index.php/category/31-motor-bikes"
        # self.houses_for_rent = "https://freelancer.homejobonline.in/index.php/houses-flats-for-rent"

    def get_adverts_links(self, URL, number_of_pages=0):
        # if advert_category == "Cars Parts":
        #     URL = self.cars_parts_link
        #
        # elif advert_category == "Motor Bikes":
        #     URL = self.motor_bikes_link

        if number_of_pages > 0:
            for current_page in range(number_of_pages):
                session = HTMLSession()
                page = session.get(URL)
                soup = BeautifulSoup(page.html.html, "html.parser")

                advert_link_prefix = "https://freelancer.homejobonline.in/index.php/all-adverts/advert/"
                connector = "?start="

                links_on_current_page = [advert_link_prefix + str(x["onclick"][56:-1]) for x in soup.findAll("img", {"itemprop": "image"})]

                URL = str(URL + connector + str(self.items_per_page*(current_page+1)))

                self.links.extend(links_on_current_page)

        else:
            self.links = [URL]

        return self.links

    def get_adverts_data(self, URL="", number_of_pages=0):
        for link in self.get_adverts_links(URL, number_of_pages):
            session = HTMLSession()
            page = session.get(link)
            soup = BeautifulSoup(page.html.html, "html.parser")

            category = "Vehicles"
            sub_category_2 = "Used Motor Bikes"
            price_unit = "Millions"
            # tag = "Sale"
            tag = "1"
            address = "."
            # location = "Indonesia"
            location = 33

            title = soup.find("title").string
            sub_category_1 = soup.find("span", {"itemprop": "category"}).string
            price_string = soup.find("div", {"class": "jomcl-right"}).string
            price = price_string[:-9] if price_string is not None else "0"
            ad_id = soup.find("span", {"itemprop": "productID"}).string
            description = soup.find("meta", {"property": "og:description"})["content"]
            more_details_name_list = [x.string for x in soup.findAll("span", {"itemprop": "name"})]
            more_details_value_list = [x.string for x in soup.findAll("span", {"itemprop": "value"})]
            image_urls_list_dirty = soup.findAll("img", {"itemprop": "image"})
            image_urls_list = [x["src"].replace("list", "gallery") for x in image_urls_list_dirty] if len(image_urls_list_dirty) > 0 else ["."]*5

            # Title, Category, 2 Sub Categories, Ad ID, Price, Price Unit, Tag, Description, Address, Location,
            details_dict = {
                "Title": title,
                # "category0": category,
                # "category1": sub_category_1,
                # "category2": sub_category_2,
                "Price": price,
                "Ad ID": ad_id,
                "Description": description,
                "Price Unit": price_unit,
                "Tag": tag,
                "Address": address,
                "Location": location,
                "topaddays": "",
                "privacy[]": "on",
                "mode": "new",
                "extImages": "",
            }

            # Price Final Status, Year, Engine Size, Mileage, Transmission, Fuel type, Color Family, Edition, Listing ID
            more_details_dict = dict(zip(more_details_name_list, more_details_value_list))

            # 5 Full Size Image URLs
            image_urls_dict = dict(zip({"Image Url 1", "Image Url 2", "Image Url 3", "Image Url 4", "Image Url 5"}, image_urls_list))

            self.data.append({**details_dict, **more_details_dict, **image_urls_dict})

        self.data[0]["title"] = self.data[0].pop("Title")
        self.data[0]["exf_26"] = self.data[0].pop("Price Final Status")
        self.data[0]["exf_27"] = self.data[0].pop("Year")
        self.data[0]["exf_28"] = self.data[0].pop("Engine Size")
        self.data[0]["exf_29"] = self.data[0].pop("Mileage")
        self.data[0]["exf_31"] = self.data[0].pop("Fuel type")
        self.data[0]["exf_32"] = self.data[0].pop("Color Family")
        self.data[0]["exf_33"] = self.data[0].pop("Edition")
        self.data[0]["exf_34"] = self.data[0].pop("Listing ID")
        self.data[0]["exf_35"] = self.data[0].pop("Ad ID")
        self.data[0]["exf_36"] = self.data[0].pop("Image Url 1")
        self.data[0]["exf_37"] = self.data[0].pop("Image Url 2")
        self.data[0]["exf_38"] = self.data[0].pop("Image Url 3")
        self.data[0]["exf_39"] = self.data[0].pop("Image Url 4")
        self.data[0]["exf_40"] = self.data[0].pop("Image Url 5")
        self.data[0]["exf_42"] = self.data[0].pop("Transmission")
        self.data[0]["currency"] = self.data[0].pop("Price Unit")
        self.data[0]["tagid"] = self.data[0].pop("Tag")
        self.data[0]["description"] = self.data[0].pop("Description")
        self.data[0]["location[]"] = self.data[0].pop("Location")
        self.data[0]["address"] = self.data[0].pop("Address")

        self.data = list(self.data[0].items())
        category_list = [("category[]", category), ("category[]", sub_category_1), ("category[]", sub_category_2)]
        self.data.extend(category_list)

        return self.data

scraper = Scraper()

print(
    scraper.get_adverts_data(
        URL="https://freelancer.homejobonline.in/index.php/all-adverts/advert/85503-yamaha-aerox-s-version"
    )
)
