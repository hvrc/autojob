from _imports import *
from advert_scraper import *
from post_ad_form_scraper import *

login_data = {}

with open("../login.txt", "r") as f:
    for line in f:
        key, value = line.split()
        login_data[key] = value

login_url = "http://newfreelancerportal.onlinecopypastejob.com/index.php/login"
post_ad_url = "http://newfreelancerportal.onlinecopypastejob.com/index.php/post-free-ad"

with open("../links.txt", "r") as f:
    links_list = [line.strip() for line in f]

for link in links_list:

    session = HTMLSession()

    # POST LOG IN FORM
    login_form = get_form(session, login_url)
    login_form_details = get_form_details(login_form)

    for input_tag in login_form_details["inputs"]:
        if input_tag["type"] == "hidden":
            login_data[input_tag["name"]] = input_tag["value"]

    login_url = urljoin(login_url, login_form_details["action"])

    # UNNECESSARY!
    # if login_form_details["method"] == "post":
    #     res = session.post(login_url, data=login_data)
    #
    # elif login_form_details["method"] == "get":
    #     res = session.get(login_url, params=login_data)

    res = session.post(login_url, data=login_data)

    # POST ADVERT FORM
    # GETTING AN ERROR HERE!
    # first ad gets posted but then during the second iteration i get an attribute
    # error. post_ad_form returns None for some fucking reason. each link which is
    # in the links.txt file works individually but when they are in a list one after
    # the other for some reason only the first one gets submitted. while scraping
    # the post form from the second link onwards, all of them return None forms.
    # also the res.text in get_form() in post_ad_form_scraper.py says "Invalid Token",
    # what does that mean? what token is invalid?
    post_ad_form = get_form(session, post_ad_url, id="jomclForm")
    post_ad_form_details = get_form_details(post_ad_form)

    # SCRAPE ADVERT DATA
    advert_data = get_advert_data(link)

    for input_tag in post_ad_form_details["inputs"]:
        if input_tag["type"] == "hidden":
            advert_data.append((input_tag["name"], input_tag["value"]))

    post_ad_url = urljoin(post_ad_url, post_ad_form_details["action"])
    res = session.post(post_ad_url, data=advert_data)

    print(str(advert_data[0][1]) + ": Advert Posted!")

    # print(res)
