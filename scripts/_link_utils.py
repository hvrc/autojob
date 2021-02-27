# returns list of links from links_archive.txt
def get_archived_links():
    links_archive_path = "../database/links_archive.txt"

    with open(links_archive_path, "r") as f:
        links_archive = [x[:-1] for x in f]

    return links_archive

# adds link to links_archive.txt
def archive_link(link):
    links_archive_path = "../database/links_archive.txt"

    with open(links_archive_path, "a") as f:
        f.write(str(link) + "\n")

# return list of links from links_to_post.txt
def get_links_to_post():
    links_to_post_path = "../database/links_to_post.txt"

    with open(links_to_post_path, "r") as f:
        links_to_post = [line.strip() for line in f]

    return links_to_post

# adds scraped links to links_to_post.txt
def save_links(list_of_links):
    links_to_post_path = "../database/links_to_post.txt"

    with open(links_to_post_path, "w") as f:
        f.writelines(list_of_links)

# adds link to links_to_recycle.txt
def recycle_link(link):
    links_to_recycle_path = "../database/links_to_recycle.txt"

    with open(links_to_recycle_path, "a") as f:
        f.write(str(link) + "\n")
