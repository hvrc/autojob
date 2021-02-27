# autojob

### Running the script

clone and run the shell script on a mac
```
$ git clone "https://github.com/hvrc/autojob.git"
$ cd autojob
$ bash run.sh
```

...on windows...
```
> git clone "https://github.com/hvrc/autojob.git"
> cd autojob
> start run.bat
```

run scripts/auto_link_fetcher.py to add links to database/links_to_post.txt,
```
$ python3 auto_link_fetcher.py
```

run scripts/main.py to start posting adverts from database/links_to_post.txt
```
$ python3 main.py
```

...on windows...
```
> python3 auto_link_fetcher.py
> python3 main.py
```

### Viewing the database

database/login.txt contains login details

database/links_archive.txt contains links that have already been posted

database/links_to_post.txt contains links (that have been scraped by scritps/auto_link_fetcher.py or have been manually added) that are yet to be posted

database/links_to_recycle.txt contains links that were not posted due to some (connection) error

