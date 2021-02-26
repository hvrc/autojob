from advert_scraper import *
from post_ad_form_scraper import *
from link_utils import *

from urllib.parse import urljoin
from requests_html import HTMLSession

import time

# posts login form
def login(session):
    login_url = "http://newfreelancerportal.onlinecopypastejob.com/index.php/login"
    login_data_path = "../database/login.txt"
    login_data = {}

    with open(login_data_path, "r") as f:
        for line in f:
            key, value = line.split()
            login_data[key] = value

    login_form = get_form(session, login_url)
    login_form_details = get_form_details(login_form)

    for input_tag in login_form_details["inputs"]:
        if input_tag["type"] == "hidden":
            login_data[input_tag["name"]] = input_tag["value"]

    login_url = urljoin(login_url, login_form_details["action"])
    res = session.post(login_url, data=login_data)

# posts advert form
def post_advert(session, link):
    post_ad_url = "http://newfreelancerportal.onlinecopypastejob.com/index.php/post-free-ad"
    success_response = lambda string : str(string) + " - Advert Posted!"
    post_ad_form = get_form(session, post_ad_url, id="jomclForm")
    post_ad_form_details = get_form_details(post_ad_form)

    advert_data = get_advert_data(link)

    for input_tag in post_ad_form_details["inputs"]:
        if input_tag["type"] == "hidden":
            advert_data.append((input_tag["name"], input_tag["value"]))

    post_ad_url = urljoin(post_ad_url, post_ad_form_details["action"])
    res = session.post(post_ad_url, data=advert_data)
    # adds posted link to links_archive.txt
    archive_link(link)
    response = success_response(advert_data[0][1])

    return response

# logs in, and posts advert
# logging in only once and trying to post multiple adverts was not working
def post(link):
    # timer to track execution time
    timer_start = time.time()
    error_1_response = "This advert has already been posted!"
    error_2_repsonse = "You've either run into a connection error, \n an unknown error or your input is incorrect!"

    session = HTMLSession()
    no_connection_error = False

    # if links has already been posted
    # TODO: populate links_archive.txt with adverts manually posted by T
    if link in get_archived_links():
        response = error_1_response

    else:
        # the only system side error encountered is a connection error while trying
        # to post an advert. keep trying to login and post, until advert is successfully
        # posted and no connection error is encountered
        while not no_connection_error:
            try:
                login(session)
                response = post_advert(session, link)
                no_connection_error = True

            except:
                response = error_2_repsonse

    timer_end = time.time()
    elapsed_time_reponse = "Finished in " + str(round(timer_end - timer_start, 2)) + " seconds"

    return response, elapsed_time_reponse
