from tkinter import *
from _poster import *

import platform
import subprocess
import webbrowser

title = "autojob"
dimensions = "400x300"
response = "."
elapsed_time = "."

def get_link_and_post():
    link = link_entry.get()
    response, elapsed_time_reponse = post(link)
    response_string.set(response)
    elapsed_time_string.set(elapsed_time_reponse)

def show_posted_links():
    links_archive_path = "../database/links_archive.txt"
    if platform.system() == "Darwin":
        subprocess.call(["open", "-a", "TextEdit", links_archive_path])
    elif platform.system() == "Windows":
        webbrowser.open(links_archive_path)
    else:
        pass

root = Tk()
root.geometry(dimensions)

frame = Frame(root)
frame.pack()

label = Label(frame, text="Enter Advert Link:")
label.pack(padx=10, pady=10)

link_entry = Entry(frame, width=20)
link_entry.pack(padx=10, pady=10)

post_advert_button = Button(frame, text="Post Advert", command=get_link_and_post)
post_advert_button.pack(padx=10, pady=10)

show_links_archive_button = Button(frame, text="Show Posted Links", command=show_posted_links)
show_links_archive_button.pack(padx=10, pady=10)

response_string = StringVar()
response_string.set(response)

response_label = Label(frame, textvariable=response_string)
response_label.pack(padx=10, pady=10)

elapsed_time_string = StringVar()
elapsed_time_string.set(elapsed_time)

elapsed_time_label = Label(frame, textvariable=elapsed_time_string)
elapsed_time_label.pack(padx=10, pady=10)

root.title(title)
root.mainloop()
