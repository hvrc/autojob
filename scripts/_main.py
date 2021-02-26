from link_utils import *
from _poster import *

if __name__ == '__main__':
    # iterates through links in links_to_post.txt
    for link in get_links_to_post():
        response, elapsed_time_reponse = post(link)
        print(response, elapsed_time_reponse)
