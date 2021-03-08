from requests_html import HTMLSession
from bs4 import BeautifulSoup

def get_advert_data(link):
    exf_dict = {
        "exf_26": "Price Final Status",
        "exf_27": "Year",
        "exf_28": "Engine Size",
        "exf_29": "Mileage",
        "exf_31": "Fuel type",
        "exf_32": "Color Family",
        "exf_33": "Edition",
        "exf_34": "Listing ID",
        "exf_42": "Transmission",
    }

    session = HTMLSession()
    page = session.get(link)
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
    address = ""
    location = "33" # "Indonesia"
    user_id = soup.find("input", {"id": "userid"})["value"]
    ad_id = soup.find("span", {"itemprop": "productID"}).string

    # scrapes the data from the table on the advert page
    more_details_name_list = [x.string for x in soup.findAll("span", {"itemprop": "name"})]
    more_details_value_list = [x.string for x in soup.findAll("span", {"itemprop": "value"})]
    image_urls_list_dirty = soup.findAll("img", {"itemprop": "image"})
    # if no images are found, then image_urls_list is populated with "."
    image_urls_list = [x["src"].replace("list", "gallery") for x in image_urls_list_dirty] if len(image_urls_list_dirty) > 0 else ["."]*5

    more_details_dict = dict(zip(more_details_name_list, more_details_value_list))
    image_urls_dict = dict(zip({"Image Url 1", "Image Url 2", "Image Url 3", "Image Url 4", "Image Url 5"}, image_urls_list))

    # the reponse variables and format were acquired by D by inspecting the post ad
    # page after manually posting an ad
    data = [
        ("title", title),

        ("category[]", category_0),
        ("category[]", category_1),
        ("category[]", category_2),

        ("exf_26", more_details_dict[exf_dict["exf_26"]] if exf_dict["exf_26"] in more_details_dict else "."),
        ("exf_27", more_details_dict[exf_dict["exf_27"]] if exf_dict["exf_27"] in more_details_dict else "."),
        ("exf_28", more_details_dict[exf_dict["exf_28"]] if exf_dict["exf_28"] in more_details_dict else "."),
        ("exf_29", more_details_dict[exf_dict["exf_29"]] if exf_dict["exf_29"] in more_details_dict else "."),
        ("exf_31", more_details_dict[exf_dict["exf_31"]] if exf_dict["exf_31"] in more_details_dict else "."),
        ("exf_32", more_details_dict[exf_dict["exf_32"]] if exf_dict["exf_32"] in more_details_dict else "."),
        ("exf_33", more_details_dict[exf_dict["exf_33"]] if exf_dict["exf_33"] in more_details_dict else "."),
        ("exf_34", more_details_dict[exf_dict["exf_34"]] if exf_dict["exf_34"] in more_details_dict else "."),
        ("exf_35", ad_id),

        ("exf_36", image_urls_dict["Image Url 1"]),
        ("exf_37", image_urls_dict["Image Url 2"]),
        ("exf_38", image_urls_dict["Image Url 3"]),
        ("exf_39", image_urls_dict["Image Url 4"]),
        ("exf_40", image_urls_dict["Image Url 5"]),

        ("exf_42", more_details_dict[exf_dict["exf_42"]] if exf_dict["exf_42"] in more_details_dict else "."),

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

        # ("latitude", ""),
        # ("langtitude", ""),
        # ("defLocation", "USA"),
        # ("7d3479d3294d40d3e0bc24756b522bd5", "1"),
    ]

    return data
