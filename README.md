# Django-website
[comment] #(python manage.py runserver) <br>
Use Django web-programming framework to implement a web server on the local host that is able to serve the following two user requests.
### Files

migration/
- generate automaticly by command make migrations<br> 


mysite/
- __init.py__
- asgi.py
- setting.py -- connect to sqlite3, static folder, etc.
- urls.py -- urls for webpages
- wsgi.py


static/
- images/
- styles.css

templates/
- index.html -- home page
- movie_insert.html -- insert page
- movies.html --main page for showing database
- results.html -- results for search engine

