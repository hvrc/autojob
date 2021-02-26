from requests_html import HTMLSession
from bs4 import BeautifulSoup

from link_utils import *

# cars_parts_link = "https://freelancer.homejobonline.in/index.php/cars-parts"
# used_cars_link = "https://freelancer.homejobonline.in/index.php/category/33-used-cars"
# houses_for_rent = "https://freelancer.homejobonline.in/index.php/houses-flats-for-rent"
motor_bikes_link = "https://freelancer.homejobonline.in/index.php/category/31-motor-bikes"
advert_link_prefix = "https://freelancer.homejobonline.in/index.php/all-adverts/advert/"

# takes url of advert category page as input and the number of pags to scrapes
def get_advert_links(URL, number_of_pages):
    items_per_page = 6
    links = []

    for current_page in range(number_of_pages):
        session = HTMLSession()
        page = session.get(URL)
        soup = BeautifulSoup(page.html.html, "html.parser")

        connector = "?start="
        links_on_current_page = [advert_link_prefix + str(x["onclick"][56:-1]) + "\n" for x in soup.findAll("img", {"itemprop": "image"})]
        URL = URL + connector + str(items_per_page*(current_page+1))
        links.extend(links_on_current_page)

    return links

if __name__ == '__main__':
    list_of_links_to_post = get_advert_links(motor_bikes_link, 1)
    save_links(list_of_links_to_post)
