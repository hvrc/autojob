from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import re

link_prefix = "http://newfreelancerportal.onlinecopypastejob.com"
category_link = link_prefix + "/index.php/all-adverts/category/33"
advert_link = link_prefix + "/index.php/all-adverts/advert/*"
links_to_post_path = "../database/links_to_post.txt"

count = 0
result = int(input("Enter page number to begin on : "))
total_pages = int(input("Enter number of pages to go through: "))

while count < total_pages:
    request = Request(category_link + "?start=" + str(6 * result - 6))
    page = urlopen(request)

    soup = BeautifulSoup(page, "lxml")
    links = []

    for link in soup.findAll("a"):
        links.append(str(link_prefix) + str((link.get("href"))))

    # final_links = []

    for link in links:
    	x = re.findall(advert_link, link)

    	if (x):
            f = open(links_to_post_path, "a")
            f.write(str(link) + "\n")
            f.close()

    count += 1
    result += 6
